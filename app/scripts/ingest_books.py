from pathlib import Path

from app.services.ingestion_service import (
    IngestionService,
)


BOOKS_PATH = Path(
    "data/book_summaries.txt"
)


def main():

    service = IngestionService()

    service.ingest(
        BOOKS_PATH
    )

    print("Books ingested successfully.")


if __name__ == "__main__":

    main()