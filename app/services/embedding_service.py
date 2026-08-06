from app.config import Settings, get_settings
from app.engine.llm.openai_provider import OpenAIProvider


class EmbeddingService:

    def __init__(
        self,
        provider: OpenAIProvider | None = None,
        settings: Settings | None = None,
    ) -> None:

        self.settings = (
            settings
            if settings is not None
            else get_settings()
        )

        self.provider = (
            provider
            if provider is not None
            else OpenAIProvider()
        )

    def create_embedding(
        self,
        text: str,
    ) -> list[float]:
        response = self.provider.client.embeddings.create(
            model=self.settings.embedding_model,
            input=text,
        )

        return response.data[0].embedding
