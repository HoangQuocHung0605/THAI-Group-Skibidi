# Ingest endpoint
# HIEC viet lai Ingest API
from fastapi import APIRouter

router = APIRouter(prefix="/api/ingest", tags=["ingest"])


@router.post("/")
def ingest():
    pass


@router.get("/status")
def get_status():
    pass
