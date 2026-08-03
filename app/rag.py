from app.embeddings import EmbeddingService
from app.vector_store import VectorStore


class RAGRetriever:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()

    def retrieve(
        self,
        query: str,
        n_results: int = 3,
    ):

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