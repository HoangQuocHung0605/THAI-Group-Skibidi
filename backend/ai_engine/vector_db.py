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
import time

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
        if not self.client.collection_exists(self.collection_name):
            print(f"[*] Đang tạo mới collection: {self.collection_name}")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,  # SỬA THÀNH 384 cho model MiniLM
                    distance=Distance.COSINE
                ),
            )

    def get_vector_store(self):
        return QdrantVectorStore(
            client=self.client,
            collection_name=self.collection_name,
            embedding=self.embeddings,
            
        )

    

    def add_documents(self, chunks, batch_size=50):
        """Nạp tài liệu theo từng đợt để tránh lỗi API và lỗi đệ quy"""
        # Lấy instance vector store từ hàm đã viết ở trên
        vector_store = self.get_vector_store()
        
        total_batches = (len(chunks) + batch_size - 1) // batch_size
        print(f"[*] Tổng số chunks: {len(chunks)} - Chia thành {total_batches} đợt nạp.")

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i : i + batch_size]
            current_batch = i // batch_size + 1
            print(f"[*] Đang nạp batch {current_batch}/{total_batches}...")
            
            # SỬA TẠI ĐÂY: Gọi hàm của vector_store, KHÔNG gọi self.add_documents
            vector_store.add_documents(batch)
            
            # Nghỉ để né hạn mức Google Free Tier
            if current_batch < total_batches:
                time.sleep(2)
        
        print("✅ Nạp dữ liệu vào Qdrant thành công!")