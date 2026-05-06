import json
from app.database import SessionLocal
from app.models.message import Message
from ai_engine.rag_chain import ask_ai 

def chat_service(question: str):
    # Gọi hàm AI đã sửa ở trên
    answer, sources = ask_ai(question)
    
    with SessionLocal() as db:
        # Lưu vào Postgres
        db_msg = Message(
            question=question,
            answer=answer,
            # Chuyển list sources thành string JSON để lưu vào cột Text
            sources=json.dumps(sources) 
        )
        db.add(db_msg)
        db.commit()
        db.refresh(db_msg)
        
    return {"answer": answer, "sources": sources}