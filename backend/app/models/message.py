# Message model
# HIEP viet lai Message model
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base  # ← import đúng từ core


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    sources = Column(Text, nullable=True)           # JSON string danh sách nguồn
    # Phải có cột này để quản lý thời gian
    created_at = Column(DateTime(timezone=True), server_default=func.now())