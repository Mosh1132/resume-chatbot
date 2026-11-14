import time
from fastapi import FastAPI
from pydantic import BaseModel, Field
from resume_chatbot.rag import ask, ask_stream
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException, Request

app = FastAPI()
session = {}
hits = {}
LIMIT = 5          # questions
WINDOW = 60        # per this many seconds

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

def check_rate_limit(ip):
    now = time.time()
    recent = [t for t in hits.get(ip, []) if now - t < WINDOW]
    if len(recent) >= LIMIT:
        raise HTTPException(status_code=429, detail="Too many questions. Please wait a minute.")
    recent.append(now)
    hits[ip] = recent

class ChatRequest(BaseModel):
    session_id : str = Field(min_length=1, max_length=64)
    question : str = Field(min_length=1, max_length=500)



@app.post("/chat")
def chat(request: ChatRequest, http_request: Request):
    check_rate_limit(http_request.client.host)
    history = session.setdefault(request.session_id, [])
    answer = ask(request.question, history)
    return {"answer": answer}

@app.post("/chat/stream")
def chat_stream(request: ChatRequest, http_request: Request):
    check_rate_limit(http_request.client.host)
    history = session.setdefault(request.session_id, [])
    return StreamingResponse(
        ask_stream(request.question, history),
        media_type="text/plain"
    )
