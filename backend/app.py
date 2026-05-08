import os
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: List[str]

app = FastAPI(title="RAG Q&A Internal")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

documents_path = os.getenv("DOCUMENTS_PATH", "./documents")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise RuntimeError("Missing OPENAI_API_KEY. Set the environment variable before running the backend.")


def load_documents(path: str):
    documents = []
    for root, _, files in os.walk(path):
        for filename in files:
            if filename.lower().endswith((".txt", ".md")):
                filepath = os.path.join(root, filename)
                loader = TextLoader(filepath, encoding="utf-8")
                documents.extend(loader.load())
    return documents


@app.on_event("startup")
def startup_event():
    global qa
    docs = load_documents(documents_path)
    if not docs:
        raise RuntimeError(f"No documents found in {documents_path}. Add .txt or .md files to the documents folder.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_llm(llm, retriever=retriever, return_source_documents=True)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    result = qa({"query": question})
    answer = result.get("result", "")
    source_documents = result.get("source_documents", [])
    sources = [doc.metadata.get("source", "Unknown") for doc in source_documents]

    return QueryResponse(answer=answer, sources=sources)
