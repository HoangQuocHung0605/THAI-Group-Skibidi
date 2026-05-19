# Chat service
# HIEP viet lai Chat service logic
from sqlalchemy.orm import Session

from ai_engine.rag_chain import RAGChain
from app.models.message import Message
from app.schemas.chat import ChatRequest, ChatResponse


class ChatService:
    def __init__(self):
        self.processor = RAGChain()

    def process_message(self, request: ChatRequest, db: Session) -> ChatResponse:
        # 1. Gọi AI engine xử lý câu hỏi
        answer = self.processor.ask(request.question)

        # 2. Lưu lịch sử vào PostgreSQL
        message = Message(
            question=request.question,
            answer=answer,
            sources="[]",
        )
        db.add(message)
        db.commit()
        db.refresh(message)

        # 3. Trả về response
        return ChatResponse(
            answer=answer,
            sources=[],
            session_id=request.session_id,
            created_at=message.created_at,
        )