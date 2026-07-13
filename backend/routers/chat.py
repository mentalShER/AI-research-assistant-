from fastapi import APIRouter
from schemas.chat import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    return {
        "reply": "Hello! I'm your AI Assistant."
    }