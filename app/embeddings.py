from openai import OpenAI

from app.config import get_settings


class EmbeddingService:
    def __init__(self) -> None:
        self.settings = get_settings()
        self.client = OpenAI(
            api_key=self.settings.openai_api_key
        )

    def create_embedding(
        self,
        text: str,
    ) -> list[float]:
        response = self.client.embeddings.create(
            model=self.settings.embedding_model,
            input=text,
        )

        return response.data[0].embedding