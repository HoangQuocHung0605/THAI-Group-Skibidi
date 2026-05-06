from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.history import router as history_router
from app.database import engine, Base
from app.models.message import Message  # Import này để Base biết bảng Message mà tạo

# Lệnh này giúp tự động tạo bảng 'messages' trong Postgres nếu chưa có
# Cực kỳ quan trọng để tránh lỗi "Relation does not exist"
Base.metadata.create_all(bind=engine)

app = FastAPI(title="RAG Chatbot API")

# Đăng ký các cổng kết nối (Endpoints)
app.include_router(chat_router, tags=["Chat"])
app.include_router(history_router, tags=["History"])

@app.get("/")
def root():
    return {"message": "Backend RAG đang chạy ngon lành rồi nhé!"}