from pathlib import Path

from app.repositories import ChromaBookRepository
from app.services.embedding_service import EmbeddingService


class IngestionService:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.repository = ChromaBookRepository()

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

        for index, book in enumerate(books):

            title = book.split("\n")[0].strip()

            embedding = (
                self.embedding_service.create_embedding(
                    book
                )
            )

            self.repository.add_document(
                document_id=f"book_{index+1}",
                document=book,
                embedding=embedding,
                metadata={
                    "title": title,
                },
            )