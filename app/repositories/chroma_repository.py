from typing import Any

import chromadb

from app.common.exceptions import RepositoryError
from app.config import get_settings
from app.repositories.base import BookRepository


class ChromaBookRepository(BookRepository):

    def __init__(self) -> None:
        self.settings = get_settings()

        self.client = chromadb.PersistentClient(
            path=self.settings.chroma_db_path
        )

        self.collection = self.client.get_or_create_collection(
            name=self.settings.collection_name
        )

    def add_document(
        self,
        document_id: str,
        document: str,
        embedding: list[float],
        metadata: dict[str, Any],
    ) -> None:
        try:
            self.collection.upsert(
                ids=[document_id],
                documents=[document],
                embeddings=[embedding],
                metadatas=[metadata],
            )
        except Exception as exc:
            raise RepositoryError(
                f"Failed to add document: {exc}"
            ) from exc

    def search(
        self,
        embedding: list[float],
        n_results: int,
        where: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        try:
            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=n_results,
                where=where,
            )

            ids = results.get("ids", [[]])[0]
            documents = results.get("documents", [[]])[0]
            metadatas = results.get("metadatas", [[]])[0]
            distances = results.get("distances", [[]])[0]

            return [
                {
                    "id": document_id,
                    "document": document,
                    "metadata": metadata,
                    "distance": distance,
                }
                for document_id, document, metadata, distance in zip(
                    ids,
                    documents,
                    metadatas,
                    distances,
                )
            ]

        except Exception as exc:
            raise RepositoryError(
                f"Vector search failed: {exc}"
            ) from exc

    def count_documents(self) -> int:
        try:
            return self.collection.count()
        except Exception as exc:
            raise RepositoryError(
                f"Failed to count documents: {exc}"
            ) from exc

    def delete_document(
        self,
        document_id: str,
    ) -> None:
        try:
            self.collection.delete(
                ids=[document_id]
            )
        except Exception as exc:
            raise RepositoryError(
                f"Failed to delete document: {exc}"
            ) from exc