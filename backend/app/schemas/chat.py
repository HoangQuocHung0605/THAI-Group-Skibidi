# Chat schema
# HIEP viet lai Chat schema
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class ChatRequest(BaseModel):
    question: str
    session_id: Optional[str] = None  # để phân biệt các cuộc hội thoại


class SourceDocument(BaseModel):
    content: str
    source: str
    score: Optional[float] = None


class ChatResponse(BaseModel):
    answer: str
    sources: List[SourceDocument] = []
    session_id: Optional[str] = None
    created_at: Optional[datetime] = None