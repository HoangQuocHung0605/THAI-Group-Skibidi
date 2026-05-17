import os
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

def get_embedding_model():
    """
    Hàm này vẫn giữ tên get_gemini_embeddings để tương thích với các file cũ,
    nhưng thực chất bên trong đã chuyển sang dùng FastEmbed.
    """
    # Sử dụng FastEmbed (cực nhẹ, không cần tải PyTorch, vector size = 384)
    # Tốc độ tải và tốc độ xử lý nhanh hơn rất nhiều!
    embeddings = FastEmbedEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        cache_dir="/app/local_model_cache"
    )
    return embeddings