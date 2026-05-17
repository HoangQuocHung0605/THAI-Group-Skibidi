import os
import sys
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

# Tìm đường dẫn tuyệt đối đến file .env
# Giả sử file .env nằm ở thư mục gốc THAI-Group-Skibidi
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Fix đường dẫn để import được VectorDBManager
root_path = Path(__file__).resolve().parent.parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))
import sys
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv # Quan trọng: Để đọc file .env

# Load các biến môi trường từ .env (như GROQ_API_KEY)
load_dotenv()

# Fix đường dẫn để import được VectorDBManager
root_path = Path(__file__).resolve().parent.parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

from backend.ai_engine.vector_db import VectorDBManager

class RAGChain:
    def __init__(self, db_manager=None):
        # 1. Kết nối VectorStore (Qdrant - Chạy local hoàn toàn)
        if db_manager:
            self.db_manager = db_manager
        else:
            self.db_manager = VectorDBManager()
            
        self.vector_store = self.db_manager.get_vector_store()
        
        # 2. Tạo Retriever để tìm 8 đoạn văn bản liên quan nhất
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 8} 
        )
        
    def _format_docs(self, docs):
        """Làm sạch dữ liệu context để AI dễ đọc"""
        formatted_context = []
        for i, doc in enumerate(docs):
            source = doc.metadata.get("source", "Handbook")
            content = doc.page_content
            formatted_context.append(f"--- Đoạn {i+1} (Nguồn: {source}) ---\n{content}")
        return "\n\n".join(formatted_context)

    def ask(self, question: str):
        """
        DÙNG GROQ ĐỂ GENERATION (PHÁT NGÔN)
        """
        try:
            # 1. Tìm tài liệu liên quan từ Database (Local Embedding)
            docs = self.retriever.invoke(question)
            context = self._format_docs(docs)
            
            # 2. Khởi tạo Client Groq
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                return "Lỗi: Không tìm thấy GROQ_API_KEY trong file .env"
                
            client = Groq(api_key=api_key)
            
            # 3. Gọi model Llama 3 (Cực mạnh và ổn định)
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system", 
                        "content": f"Bạn là chuyên gia về GitLab Handbook. Hãy trả lời bằng TIẾNG VIỆT dựa trên ngữ cảnh được cung cấp sau đây:\n\n{context}"
                    },
                    {
                        "role": "user", 
                        "content": question
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.2
            )
            
            return chat_completion.choices[0].message.content

        except Exception as e:
            return f"Lỗi hệ thống Groq: {str(e)}"