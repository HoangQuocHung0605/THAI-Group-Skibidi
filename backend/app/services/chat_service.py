# Chat service
# HIEP viet lai Chat service logic
import json
from sqlalchemy.orm import Session

from ai_engine.rag_chain import RAGChain
from app.models.message import Message
from app.schemas.chat import ChatRequest, ChatResponse, SourceDocument


class ChatService:
    def __init__(self):
        self.processor = RAGChain()

    def process_message(self, request: ChatRequest, db: Session) -> ChatResponse:
        # 1. Gọi AI engine xử lý câu hỏi
        result = self.processor.process(request.question)

        # 2. Lưu lịch sử vào PostgreSQL
        sources_json = json.dumps(
            [s if isinstance(s, dict) else (s.dict() if hasattr(s, 'dict') else dict(s)) for s in result.get("sources", [])],
            ensure_ascii=False
        )
        message = Message(
            question=request.question,
            answer=result["answer"],
            sources=sources_json,
        )
        db.add(message)
        db.commit()
        db.refresh(message)

        # 3. Trả về response
        sources = [
            SourceDocument(
                content=s.get("content", ""),
                source=s.get("source", ""),
                score=s.get("score"),
            )
            for s in result.get("sources", [])
        ]

        return ChatResponse(
            answer=result["answer"],
            sources=sources,
            session_id=request.session_id,
            created_at=message.created_at,
        )