from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RAG Solution - Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/chat")
def chat_endpoint():
    # HIEC Viet Lai API Chat
    pass


@app.post("/api/ingest")
def ingest_endpoint():
    # HIEC Viet Lai Ingest API
    pass


@app.get("/api/history")
def history_endpoint():
    # HIEC Viet Lai History API
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
