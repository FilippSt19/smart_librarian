import hashlib
from pathlib import Path

from app.repositories import ChromaBookRepository
from app.services.embedding_service import EmbeddingService


class IngestionService:

    def __init__(self) -> None:
        self.embedding_service = EmbeddingService()
        self.repository = ChromaBookRepository()

    @staticmethod
    def _create_document_id(
        title: str,
    ) -> str:
        normalized_title = (
            title.strip()
            .lower()
            .encode("utf-8")
        )

        title_hash = hashlib.sha256(
            normalized_title
        ).hexdigest()[:16]

        return f"book_{title_hash}"

    def ingest(
        self,
        file_path: Path,
    ) -> None:

        text = file_path.read_text(
            encoding="utf-8"
        )

        books = text.split("## Title:")

        books = [
            book.strip()
            for book in books
            if book.strip()
        ]

        for book in books:

            title = book.split("\n")[0].strip()

            embedding = (
                self.embedding_service.create_embedding(
                    book
                )
            )

            self.repository.add_document(
                document_id=self._create_document_id(
                    title
                ),
                document=book,
                embedding=embedding,
                metadata={
                    "title": title,
                },
            )