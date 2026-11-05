import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        return {"success": False, "error": "There is an issue with API Key"}
    return api_key

def get_pinecone_key():
    pinecone_key = os.environ.get("PINECONE_API_KEY")
    if not pinecone_key:
        return {"success": False, "error": "There is an issue with Pinecone Key"}
    return pinecone_key