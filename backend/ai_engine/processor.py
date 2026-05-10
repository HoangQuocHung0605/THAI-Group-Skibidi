import os
from pathlib import Path
from tqdm import tqdm
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

class GitLabHandbookProcessor:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path).resolve()
        
        # Cấu hình tách theo Header để giữ cấu trúc Handbook (Task 1 yêu cầu)
        self.headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
        
        self.md_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.headers_to_split_on, 
            strip_headers=False
        )
        
        # Bộ tách phụ để đảm bảo chunk không quá lớn
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150
        )

    def process_all(self):
        print(f"--- BẮT ĐẦU XỬ LÝ DỮ LIỆU TẠI: {self.data_path} ---")
        
        if not self.data_path.exists():
            print(f"LỖI: Thư mục không tồn tại.")
            return []

        # 1. Nạp dữ liệu: Thêm encoding='utf-8' để sửa lỗi UnicodeDecodeError
        # show_progress=True sẽ hiện thanh tiến trình của chính LangChain khi quét file
        print("1. Đang quét và nạp file Markdown...")
        loader = DirectoryLoader(
            str(self.data_path), 
            glob="**/*.md", 
            loader_cls=TextLoader,
            show_progress=True,
            use_multithreading=True,
            max_concurrency=8,
            loader_kwargs={'encoding': 'utf-8'} # SỬA LỖI Ở ĐÂY
        )
        
        try:
            raw_docs = loader.load()
            print(f"-> Thành công: Đã nạp {len(raw_docs)} file.")
        except Exception as e:
            print(f"LỖI hệ thống khi nạp file: {e}")
            return []

        # 2. Băm nhỏ văn bản (Markdown Header Splitting)
        print("2. Đang phân tích cấu trúc Header và băm nhỏ...")
        all_final_chunks = []
        
        # Dùng tqdm để hiện tiến trình băm nhỏ từng file
        for doc in tqdm(raw_docs, desc="Tiến độ Chunking", unit="file"):
            # Lấy metadata nguồn
            source_full_path = Path(doc.metadata.get("source", ""))
            try:
                rel_path = source_full_path.relative_to(self.data_path)
                source_label = str(rel_path)
            except:
                source_label = source_full_path.name

            # Tách theo Header Markdown
            header_splits = self.md_splitter.split_text(doc.page_content)
            
            # Tách nhỏ tiếp những đoạn Header quá dài
            final_splits = self.text_splitter.split_documents(header_splits)
            
            for chunk in final_splits:
                chunk.metadata["source_path"] = source_label
                all_final_chunks.append(chunk)
            
        print(f"\n=== HOÀN THÀNH ===")
        print(f"Tổng cộng nạp được: {len(raw_docs)} file.")
        print(f"Tổng cộng tạo ra: {len(all_final_chunks)} đoạn văn bản (chunks).")
        return all_final_chunks

if __name__ == "__main__":
    # Xác định đường dẫn tương đối từ file processor.py
    BASE_DIR = Path(__file__).resolve().parent
    # Đi ngược lên 2 cấp để vào thư mục data/handbook
    DATA_DIR = BASE_DIR.parent.parent / "data" / "handbook"
    
    processor = GitLabHandbookProcessor(str(DATA_DIR))
    final_data = processor.process_all()
    
    if final_data:
        print("\n--- KIỂM TRA ĐOẠN ĐẦU TIÊN ---")
        sample = final_data[0]
        print(f"Nguồn: {sample.metadata.get('source_path')}")
        print(f"Headers: { {k:v for k,v in sample.metadata.items() if 'Header' in k} }")
        print(f"Nội dung: {sample.page_content[:200]}...")