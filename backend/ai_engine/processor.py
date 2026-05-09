# AI Engine - Processor
# HIEP viet lai Processor
from ai_engine.rag_chain import ask_ai


class Processor:
    def process(self, question: str) -> dict:
        """
        Nhận câu hỏi, gọi RAG chain, trả về dict chuẩn cho ChatService
        """
        answer, sources = ask_ai(question)
        return {
            "answer": answer,
            "sources": sources,
        }