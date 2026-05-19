# Message schema
# HIEP viet lai Message schema
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MessageBase(BaseModel):
    question: str
    answer: str
    sources: Optional[str] = None


class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

    class Config:
        from_attributes = True  # cho phép đọc từ SQLAlchemy model