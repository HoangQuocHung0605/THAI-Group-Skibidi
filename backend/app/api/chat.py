# Chat endpoint
# HIEC viet lai Chat API
from fastapi import APIRouter

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("/")
def chat():
    pass


@router.get("/history")
def get_history():
    pass
