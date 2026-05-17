import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_embedding_model():
    """
    Khởi tạo Embedding Model từ Google Gemini.
    Đảm bảo GOOGLE_API_KEY đã có trong file .env
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Lỗi: Không tìm thấy GOOGLE_API_KEY. Vui lòng kiểm tra file .env")

    # Sử dụng text-embedding-004 (phiên bản mới nhất, hiệu suất cao hơn 001)
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=api_key
    )
    return embeddings