import os
from pathlib import Path
from tqdm import tqdm
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class GitLabHandbookProcessor:
    def __init__(self, data_path: str):
        """
        Khởi tạo Processor cho toàn bộ dữ liệu Handbook đã lọc.
        """
        self.data_path = Path(data_path).resolve()
        
        # Cấu hình Chunking chuẩn cho RAG
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200, 
            add_start_index=True,
            separators=["\n\n", "\n", " ", ""]
        )

    def process_all(self):
        print(f"--- BẮT ĐẦU XỬ LÝ TOÀN BỘ DATA TẠI: {self.data_path} ---")
        
        if not self.data_path.exists():
            print(f"LỖI: Thư mục không tồn tại.")
            return []

        # 1. Nạp dữ liệu với cơ chế Đa luồng (Multithreading) để không bị treo
        print("1. Đang nạp các file Markdown (Hùng đợi thanh tiến trình hiện nhé)...")
        loader = DirectoryLoader(
            str(self.base_path if hasattr(self, 'base_path') else self.data_path), 
            glob="**/*.md", 
            loader_cls=UnstructuredMarkdownLoader,
            show_progress=True,      # Hiện tiến trình nạp file
            use_multithreading=True, # Dùng nhiều lõi CPU
            max_concurrency=8        # Xử lý song song 8 file cùng lúc
        )
        
        try:
            raw_docs = loader.load()
            print(f"-> Thành công: Đã nạp {len(raw_docs)} file.")
        except Exception as e:
            print(f"LỖI khi nạp file: {e}")
            return []

        # 2. Băm nhỏ văn bản (Chunking)
        print("2. Đang băm nhỏ dữ liệu thành các đoạn kiến thức...")
        all_chunks = []
        
        # Dùng tqdm để Hùng thấy tiến độ băm từng file
        for doc in tqdm(raw_docs, desc="Tiến độ Chunking", unit="file"):
            chunks = self.text_splitter.split_documents([doc])
            
            # Lưu Metadata thông minh: Lấy đường dẫn tương đối để AI biết file nằm ở folder nào
            source_full_path = Path(doc.metadata.get("source", ""))
            try:
                # Lưu đường dẫn từ sau chữ 'handbook' để trích dẫn cho đẹp
                rel_path = source_full_path.relative_to(self.data_path)
                source_label = str(rel_path)
            except:
                source_label = source_full_path.name

            for chunk in chunks:
                chunk.metadata["source_path"] = source_label
                all_chunks.append(chunk)
            
        print(f"\n=== HOÀN THÀNH XỬ LÝ DỮ LIỆU ===")
        print(f"Tổng cộng nạp được: {len(raw_docs)} file.")
        print(f"Tổng cộng tạo ra: {len(all_chunks)} đoạn văn bản (chunks).")
        return all_chunks

if __name__ == "__main__":
    # Tự động xác định đường dẫn
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR.parent.parent / "data" / "handbook"
    
    # Khởi tạo và chạy
    processor = GitLabHandbookProcessor(str(DATA_DIR))
    final_data = processor.process_all()
    
    # Kiểm tra thử 1 đoạn bất kỳ
    if final_data:
        print("\n--- VÍ DỤ MỘT ĐOẠN DỮ LIỆU ---")
        sample = final_data[0]
        print(f"Nguồn: {sample.metadata['source_path']}")
        print(f"Nội dung: {sample.page_content[:150]}...")