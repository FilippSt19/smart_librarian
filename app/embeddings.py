from openai import OpenAI

from app.config import OPENAI_API_KEY, EMBEDDING_MODEL


class EmbeddingService:
    """
    Service responsible for generating embeddings using OpenAI.
    """

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def create_embedding(self, text: str) -> list[float]:
        """
        Generate an embedding for a given text.
        """

        response = self.client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=text
        )

        return response.data[0].embedding