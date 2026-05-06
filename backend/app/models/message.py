from app.database import Base # Thêm dòng này để định nghĩa Base
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    answer = Column(Text)
    sources = Column(Text)
    # Phải có cột này để quản lý thời gian
    created_at = Column(DateTime(timezone=True), server_default=func.now())