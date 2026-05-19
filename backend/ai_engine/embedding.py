from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model():
    # Model đa ngôn ngữ, hỗ trợ cực tốt cho cặp Anh - Việt
    model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    
    # Chạy trên CPU (nếu bạn có GPU NVIDIA thì đổi thành 'cuda')
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': True} # Normalize để so sánh Cosine chính xác hơn
    
    print(f"[*] Đang khởi tạo Local Embedding Model: {model_name}...")
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embeddings