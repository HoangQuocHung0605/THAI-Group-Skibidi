from fastapi import APIRouter
from app.database import SessionLocal
from app.models.message import Message

router = APIRouter()

# Trong file app/api/history.py
@router.get("/history")
def get_history():
    with SessionLocal() as db:
        # Thêm .order_by để sắp xếp theo thời gian giảm dần
        messages = db.query(Message).order_by(Message.created_at.desc()).all()
        return messages