# RAG Chain module
# HIEP viet lai RAG Chain logic
from langchain_google_genai import ChatGoogleGenerativeAI
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
    # Check if Google API key is configured
    if not settings.GOOGLE_API_KEY:
        # Check fallback to OpenAI
        if not settings.OPENAI_API_KEY or settings.OPENAI_API_KEY.startswith("sk-placeholder"):
            return f"Demo response: {question}", []
    
    try:
        vdb = VectorDB()
        retriever = vdb.as_retriever()

        if settings.GOOGLE_API_KEY:
            llm = ChatGoogleGenerativeAI(
                google_api_key=settings.GOOGLE_API_KEY,
                model=settings.GEMINI_MODEL,
                temperature=0,
            )
        else:
            from langchain_openai import ChatOpenAI
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