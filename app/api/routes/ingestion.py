from pathlib import Path

from fastapi import APIRouter, HTTPException, status

from app.services.ingestion_service import IngestionService


router = APIRouter(
    prefix="/ingestion",
    tags=["Ingestion"],
)


@router.post(
    "/books",
    status_code=status.HTTP_200_OK,
)
def ingest_books():

    try:

        service = IngestionService()

        service.ingest(
            Path(
                "data/book_summaries.txt"
            )
        )

        return {
            "message": "Books ingested successfully."
        }

    except Exception as exc:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc