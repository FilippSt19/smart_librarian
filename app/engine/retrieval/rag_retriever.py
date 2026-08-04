from app.config import get_settings
from app.services.embedding_service import (
    EmbeddingService,
)
from app.vector_store import VectorStore


class RAGRetriever:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.settings = get_settings()

    def retrieve(
        self,
        query: str,
        n_results: int | None = None,
    ):
        n_results = (
            n_results
            if n_results is not None
            else self.settings.default_n_results
        )

        query_embedding = self.embedding_service.create_embedding(
            query
        )

        results = self.vector_store.search(
            embedding=query_embedding,
            n_results=n_results,
        )

        return [
            {
                "title": result["metadata"]["title"],
                "document": result["document"],
            }
            for result in results
        ]
