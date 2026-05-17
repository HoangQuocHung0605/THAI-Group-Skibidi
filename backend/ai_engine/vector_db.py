import os
from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_community.vectorstores import Qdrant as QdrantVectorStore
from ai_engine.embedding import get_embedding_model


class VectorDBManager:
    def __init__(self):
        self.collection_name = "gitlab_handbook"

        # Khởi tạo embedding model từ file embeddings.py
        self.embeddings = get_embedding_model()

        # Kết nối tới Qdrant server qua URL (Docker container)
        qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
        qdrant_api_key = os.getenv("QDRANT_API_KEY", None)

        self.client = QdrantClient(
            url=qdrant_url,
            api_key=qdrant_api_key,
        )
        self._ensure_collection()

    def _ensure_collection(self):
        """Tạo collection nếu chưa tồn tại"""
        if not self.client.collection_exists(self.collection_name):
            print(f"[*] Đang tạo mới collection: {self.collection_name}")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,  # Kích thước vector của all-MiniLM-L6-v2 là 384
                    distance=Distance.COSINE
                ),
            )

    def get_vector_store(self):
        """Trả về instance QdrantVectorStore để dùng cho RAG chain"""
        return QdrantVectorStore(
            client=self.client,
            collection_name=self.collection_name,
            embeddings=self.embeddings,
        )

    def add_documents(self, documents):
        """Lưu danh sách Document vào Qdrant"""
        vector_store = self.get_vector_store()
        vector_store.add_documents(documents)
        print(f"[+] Đã lưu {len(documents)} chunks vào Qdrant thành công.")
