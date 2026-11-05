import os
import time
from resume_chatbot.config import get_api_key, get_pinecone_key
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key=get_pinecone_key())
index_name = "resume"

current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, "..", "..", "data", "resume.pdf")
loader = PyPDFLoader(file_path=pdf_path)
document = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(document)
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
        index_name="resume",
        embedding=embeddings,
        documents=chunks
    )

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={'k':5})

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=get_api_key()
)


def ask(query, history):
    relevant_docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    # recent_history = history[-5:]

    history_text = "\n".join([f"'user': {q}, 'assistant': {a}" for q, a in history])

    prompt = f"""
        Use the context below to answer the question

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
