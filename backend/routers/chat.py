from fastapi import APIRouter
from schemas.chat import ChatRequest
from services.chat_service import generate_reply


router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    reply = generate_reply(request.message)

    return {
        "reply": reply
    }