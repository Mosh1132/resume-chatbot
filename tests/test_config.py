from resume_chatbot.config import get_api_key, get_pinecone_key

def test_get_api_key_returns_key(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "test_key")
    assert "test_key" == get_api_key()

def test_get_api_key_returns_error_when_no_key(monkeypatch):
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    assert "error" in get_api_key()

def test_get_pinecone_key_returns_key(monkeypatch):
    monkeypatch.setenv("PINECONE_API_KEY", "test_key")
    assert "test_key" == get_pinecone_key()

def test_get_pinecone_key_returns_error_when_no_key(monkeypatch):
    monkeypatch.delenv("PINECONE_API_KEY", raising=False)
    assert "error" in get_pinecone_key()