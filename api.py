from fastapi import FastAPI
from pydantic import BaseModel
from resume_chatbot.rag import ask, ask_stream
from fastapi.responses import StreamingResponse

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

@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    history = session.setdefault(request.session_id, [])
    return StreamingResponse(
        ask_stream(request.question, history),
        media_type="text/plain"
    )
