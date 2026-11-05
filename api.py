from fastapi import FastAPI
from pydantic import BaseModel
from resume_chatbot.rag import ask

app = FastAPI()

class ChatRequest(BaseModel):
    session_id : str
    question : str

session = {}

@app.post("/chat")
def chat(request: ChatRequest):
    history = session.setdefault(request.session_id, [])
    answer = ask(request.question, history)
    return {"answer": answer}
