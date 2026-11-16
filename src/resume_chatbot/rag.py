import os
import time
from resume_chatbot.config import get_api_key, get_pinecone_key
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=get_pinecone_key())
index_name = "knowledge"

current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "..", "..", "data", "knowledge.md")
loader = TextLoader(file_path=pdf_path, encoding="utf-8")
document = loader.load()
header_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=([('##', 'section')]))
sections = header_splitter.split_text(document[0].page_content)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(sections)
for c in chunks:
    c.page_content = f"{c.metadata.get('section', '')}\n{c.page_content}"
embeddings = OpenAIEmbeddings(api_key=get_api_key())

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

    index = pc.Index(index_name)
    PineconeVectorStore.from_documents(
        index_name="knowledge",
        embedding=embeddings,
        documents=chunks
    )

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={'k':5})

llm = ChatOpenAI(
    model="gpt-6-luna",
    api_key=get_api_key(),
    max_tokens=200
)
def get_docs(query):
    return retriever.invoke(query)


def get_sources(docs):
    seen = []
    for d in docs:
        s = d.metadata.get("section")
        if s and s not in seen:
            seen.append(s)
    return seen

def ask(query, history):
    relevant_docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    history_text = "\n".join([f"'user': {q}, 'assistant': {a}" for q, a in history])

    prompt = f"""
        You are an AI assistant that answers recruiters' questions about Mosh Oluwashina.
        Use only the context below. Refer to him as "Mosh" or "he", never "I".
        Keep answers short: 2 to 3 sentences, starting with the most relevant fact. Do not list everything.
        If the question is about the portfolio website or the Resume RAG, say that this chat is the Resume RAG and the 
        visitor is using Mosh's portfolio website right now.
        If the answer is not in the context, say "I don't have that information."

        Conversation History:
        {history_text}

        Context:
        {context}

        Question:
        {query}
"""
    response = llm.invoke(prompt)
    history.append((query, response.content))
    return response.content


def ask_stream(query, history, docs):
    context = "\n\n".join([doc.page_content for doc in docs])
    history_text = "\n".join([f"'user': {q}, 'assistant': {a}" for q, a in history])

    prompt = f"""
       You are an AI assistant on Mosh Oluwashina's portfolio site. You answer recruiters' questions about Mosh, 
       speaking as Mosh in the first person ("I built...", "my project...").

        Rules:
        1. Use only the context below. Never invent facts, numbers, or projects that are not in it.
        2. If the answer is not in the context, reply with exactly: I don't have that information.
        3. The context is written about "Mosh" in the third person. Rewrite facts in the first person.
        4. Keep answers to 2 to 3 sentences, starting with the most relevant fact. Do not list everything.


        Conversation History:
        {history_text}

        Context:
        {context}

        Question:
        {query}
"""
    full_answer = ""
    for chunk in llm.stream(prompt):
        if chunk:
            full_answer += chunk.content
            yield chunk.content

    history.append((query, full_answer))

def classifier(question):
    prompt = [{
        "role": "system",
        "content": """You are a classifier. Read the visitor's question and reply with exactly one word: future or now.
            Reply "future" if the question asks about projects that are not finished yet. This includes projects that are:
            - in the making, in the works, or being made
            - planned, upcoming, or about to drop
            - what the person is building or working on next
            - anything else about future projects (for example "any new projects coming?", "what's next?", "are you building anything right now?")
            
            Reply "now" for everything else. This includes:
            - questions about projects that already exist or are finished
            - questions about skills, experience, education, or contact details
            - greetings and any other topic
            
            Rules:
            - Reply with only the single word future or now. No punctuation, no explanation, no other text.
            - If you are unsure, reply now.
            
            Examples:
            Question: any more projects on the way? -> future
            Question: have any others in the making? -> future
            Question: what are you working on next? -> future
            Question: anything about to drop? -> future
            Question: what projects have you built? -> now
            Question: tell me about your resume chatbot -> now
            Question: what are your skills? -> now
            Question: do you have any other projects? -> now"""
    },
        {
         "role": "user",
            "content":question
        }
    ]
    label = llm.invoke(prompt)
    return label.content