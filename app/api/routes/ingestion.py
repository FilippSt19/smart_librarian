from pathlib import Path

from fastapi import APIRouter

from app.services.ingestion_service import (
    IngestionService,
)


router = APIRouter(
    prefix="/ingestion",
    tags=["Ingestion"],
)


@router.post("/books")
def ingest_books():

    service = IngestionService()

    service.ingest(
        Path(
            "data/book_summaries.txt"
        )
    )

    return {
        "message":
        "Books ingested successfully."
    }