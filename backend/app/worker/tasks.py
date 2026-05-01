# Celery tasks
# HIEC viet lai Celery background tasks
from celery import Celery

app = Celery("rag_solution", broker="redis://localhost:6379")


@app.task
def process_document(doc_id: str):
    pass


@app.task
def generate_embedding(text: str):
    pass
