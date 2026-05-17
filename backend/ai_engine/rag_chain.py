from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from ai_engine.vector_db import VectorDBManager

class RAGChain:
    def __init__(self):
        # 1. Khởi tạo LLM
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            temperature=0.1, # Giảm thêm để tăng độ chính xác
        )
        
        # 2. Khởi tạo VectorStore
        self.db_manager = VectorDBManager()
        self.vector_store = self.db_manager.get_vector_store()
        
        # 3. Tạo Retriever với cấu hình tối ưu
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 8} 
        )
        
        # 4. Prompt chuyên nghiệp hơn
        self.prompt = ChatPromptTemplate.from_template("""
Bạn là chuyên gia về quy trình nội bộ tại GitLab. 
Nhiệm vụ của bạn là trả lời câu hỏi dựa TRỰC TIẾP vào ngữ cảnh được cung cấp dưới đây.

YÊU CẦU:
1. Nếu thông tin không có trong ngữ cảnh, hãy nói rõ: "Tôi xin lỗi, thông tin này không được đề cập trong GitLab Handbook."
2. Trả lời súc tích, rõ ràng, trình bày dạng danh sách nếu có nhiều ý.
3. Luôn giữ thái độ chuyên nghiệp.

NGỮ CẢNH:
{context}

CÂU HỎI: 
{question}

TRẢ LỜI:
""")

    def _format_docs(self, docs):
        """Hàm bổ trợ để làm sạch dữ liệu context trước khi nạp vào Prompt"""
        formatted_context = []
        for i, doc in enumerate(docs):
            source = doc.metadata.get("source", "Không rõ nguồn")
            header = doc.metadata.get("Header 1", "")
            content = doc.page_content
            formatted_context.append(f"--- Đoạn {i+1} (Nguồn: {source} > {header}) ---\n{content}")
        return "\n\n".join(formatted_context)

    def get_chain(self):
        # Sử dụng pipe để xử lý context qua hàm format_docs
        chain = (
            {
                "context": self.retriever | self._format_docs, 
                "question": RunnablePassthrough()
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        return chain

    def ask(self, question: str):
        # Khi làm việc nhóm, việc dùng try-except ở đây giúp API không bị crash nếu mất mạng/hết quota
        try:
            chain = self.get_chain()
            return chain.invoke(question)
        except Exception as e:
            return f"Đã xảy ra lỗi khi kết nối với AI: {str(e)}"

    def process(self, question: str):
        try:
            docs = self.retriever.invoke(question)
            chain = self.get_chain()
            answer = chain.invoke(question)
            
            sources = []
            for doc in docs:
                sources.append({
                    "content": doc.page_content,
                    "source": doc.metadata.get("source", "Không rõ nguồn"),
                    "score": 0.0
                })
            return {"answer": answer, "sources": sources}
        except Exception as e:
            return {
                "answer": f"Đã xảy ra lỗi khi kết nối với AI: {str(e)}",
                "sources": []
            }
