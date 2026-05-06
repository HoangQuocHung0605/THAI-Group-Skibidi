from fastapi import APIRouter
from app.services.chat_service import chat_service

router = APIRouter()

@router.post("/chat")
async def chat_api(request: dict):
    question = request.get("question")
    answer = chat_service(question)
    return {"answer": answer}