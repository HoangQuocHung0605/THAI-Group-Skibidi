# Vector Database module
# HIEP viet lai Vector DB integration
from typing import List
from langchain_community.vectorstores import Qdrant
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from app.core.config import settings


class VectorDB:
    def __init__(self):
        self.client = QdrantClient(url=settings.QDRANT_URL)
        if settings.GOOGLE_API_KEY:
            self.embeddings = GoogleGenerativeAIEmbeddings(
                google_api_key=settings.GOOGLE_API_KEY,
                model=settings.GOOGLE_EMBEDDING_MODEL,
            )
        elif settings.OPENAI_API_KEY and not settings.OPENAI_API_KEY.startswith("sk-placeholder"):
            # Fallback to OpenAI if needed, but the goal is Gemini
            from langchain_openai import OpenAIEmbeddings
            self.embeddings = OpenAIEmbeddings(
                openai_api_key=settings.OPENAI_API_KEY,
                model=settings.EMBEDDING_MODEL,
            )
        else:
            self.embeddings = None
        self.collection_name = settings.QDRANT_COLLECTION
        self._ensure_collection()

    def _ensure_collection(self):
        """Tạo collection nếu chưa có"""
        existing = [c.name for c in self.client.get_collections().collections]
        if self.collection_name not in existing:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
            )

    def add_documents(self, content: str, metadata: dict = {}) -> int:
        """Chia nhỏ và đưa văn bản vào Qdrant, trả về số chunks"""
        if not self.embeddings:
            raise RuntimeError("Google API key not configured. Cannot add documents.")
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
        )
        chunks = splitter.split_text(content)

        vectorstore = Qdrant(
            client=self.client,
            collection_name=self.collection_name,
            embeddings=self.embeddings,
        )
        vectorstore.add_texts(
            texts=chunks,
            metadatas=[metadata] * len(chunks),
        )
        return len(chunks)

    def as_retriever(self):
        """Trả về retriever để RAG chain dùng"""
        if not self.embeddings:
            raise RuntimeError("OpenAI API key not configured. Cannot create retriever.")
        vectorstore = Qdrant(
            client=self.client,
            collection_name=self.collection_name,
            embeddings=self.embeddings,
        )
        return vectorstore.as_retriever(search_kwargs={"k": 4})

    def embed_text(self, text: str) -> List[float]:
        """Tạo embedding cho một đoạn text"""
        if not self.embeddings:
            raise RuntimeError("OpenAI API key not configured. Cannot embed text.")
        return self.embeddings.embed_query(text)

    def count(self) -> int:
        """Trả về số lượng chunks trong collection"""
        info = self.client.get_collection(self.collection_name)
        return info.points_count