import sys
from pathlib import Path

# Thêm thư mục gốc (THAI-Group-Skibidi) vào hệ thống tìm kiếm module
root_path = str(Path(__file__).resolve().parent.parent.parent)
if root_path not in sys.path:
    sys.path.append(root_path)
import os
from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from backend.ai_engine.embedding import get_embedding_model

class VectorDBManager:
    def __init__(self):
        # Xác định đường dẫn: backend/ai_engine/vector_db.py -> lên 2 cấp -> data/qdrant
        base_dir = Path(__file__).resolve().parent.parent.parent
        self.db_path = base_dir / "data" / "qdrant"
        self.collection_name = "gitlab_handbook"
        
        # Khởi tạo embedding model từ file embeddings.py
        self.embeddings = get_embedding_model()
        
        # Khởi tạo Qdrant Client (Local mode)
        self.client = QdrantClient(path=str(self.db_path))
        self._ensure_collection()

    def _ensure_collection(self):
        """Tạo collection nếu chưa tồn tại"""
        if not self.client.collection_exists(self.collection_name):
            print(f"[*] Đang tạo mới collection: {self.collection_name}")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=768, # Kích thước vector của Gemini là 768
                    distance=Distance.COSINE
                ),
            )

    def get_vector_store(self):
        """Trả về instance QdrantVectorStore để dùng cho RAG chain"""
        return QdrantVectorStore(
            client=self.client,
            collection_name=self.collection_name,
            embedding=self.embeddings,
        )

    def add_documents(self, documents):
        """Lưu danh sách Document vào Qdrant"""
        vector_store = self.get_vector_store()
        vector_store.add_documents(documents)
        print(f"[+] Đã lưu {len(documents)} chunks vào Qdrant thành công.")
