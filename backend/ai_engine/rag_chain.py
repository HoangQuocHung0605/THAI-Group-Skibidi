# RAG Chain module
# HIEP viet lai RAG Chain logic
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from app.core.config import settings
from ai_engine.vector_db import VectorDB


PROMPT_TEMPLATE = """Bạn là trợ lý AI thông minh. Hãy trả lời câu hỏi dựa trên ngữ cảnh được cung cấp.
Nếu không tìm thấy thông tin trong ngữ cảnh, hãy nói rõ là bạn không biết.
Trả lời bằng tiếng Việt.

Ngữ cảnh:
{context}

Câu hỏi: {question}

Trả lời:"""


def ask_ai(question: str) -> tuple:
    """
    Trả về 2 giá trị: 1 chuỗi (answer) và 1 danh sách (sources)
    """
    # Check if API key is configured
    if not settings.OPENAI_API_KEY or settings.OPENAI_API_KEY.startswith("sk-placeholder"):
        return f"Demo response: {question}", []
    
    try:
        vdb = VectorDB()
        retriever = vdb.as_retriever()

        llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=settings.OPENAI_MODEL,
            temperature=0,
        )

        prompt = PromptTemplate(
            template=PROMPT_TEMPLATE,
            input_variables=["context", "question"],
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt},
        )

        result = qa_chain.invoke({"query": question})
        answer = result.get("result", "")
        source_docs = result.get("source_documents", [])
        sources = [
            {
                "content": doc.page_content[:200],
                "source": doc.metadata.get("source", "Unknown"),
                "score": doc.metadata.get("score"),
            }
            for doc in source_docs
        ]

        return answer, sources
    except Exception as e:
        return f"Error processing question: {str(e)}", []