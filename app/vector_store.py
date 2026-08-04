from app.config import get_settings
from typing import Any

import chromadb

# from .config import CHROMA_DB_PATH, COLLECTION_NAME


from app.config import Config
class VectorStore:
    """
    Handles all interactions with the ChromaDB vector database.
    """

    def __init__(self) -> None:
        self.client = chromadb.PersistentClient(
            path=Config.CHROMA_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=Config.COLLECTION_NAME
        )

    def add_document(
        self,
        document_id: str,
        document: str,
        embedding: list[float],
        metadata: dict[str, Any],
    ) -> None:
        """
        Add or update a document in the vector store.
        """

        try:
            self.collection.upsert(
                ids=[document_id],
                documents=[document],
                embeddings=[embedding],
                metadatas=[metadata],
            )
        except Exception as exc:
            raise RuntimeError(f"Failed to add document: {exc}") from exc

    def count_documents(self) -> int:
        """
        Return the total number of indexed documents.
        """

        try:
            return self.collection.count()
        except Exception as exc:
            raise RuntimeError(f"Failed to count documents: {exc}") from exc

    def search(
        self,
        embedding: list[float],
        n_results: int = 3,
        where: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """
        Search for the most similar documents.

        Args:
            embedding: Query embedding.
            n_results: Number of results to return.
            where: Optional metadata filter.

        Returns:
            A list of dictionaries containing:
                - id
                - document
                - metadata
                - distance
        """

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
                    "id": doc_id,
                    "document": document,
                    "metadata": metadata,
                    "distance": distance,
                }
                for doc_id, document, metadata, distance in zip(
                    ids,
                    documents,
                    metadatas,
                    distances,
                )
            ]

        except Exception as exc:
            raise RuntimeError(f"Vector search failed: {exc}") from exc

    def delete_document(self, document_id: str) -> None:
        """
        Delete a document from the vector store.
        """

        try:
            self.collection.delete(ids=[document_id])
        except Exception as exc:
            raise RuntimeError(f"Failed to delete document: {exc}") from exc