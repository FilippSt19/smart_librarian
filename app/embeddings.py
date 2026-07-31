from openai import APIConnectionError, OpenAI

from app.config import OPENAI_API_KEY, EMBEDDING_MODEL


class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def create_embedding(self, text: str) -> list[float]:
        try:
            response = self.client.embeddings.create(
                model=EMBEDDING_MODEL,
                input=text,
            )
            return response.data[0].embedding

        except APIConnectionError as exc:
            raise RuntimeError(
                "Nu s-a putut realiza conexiunea la OpenAI. "
                "Verifică DNS-ul, VPN-ul, proxy-ul și firewall-ul."
            ) from exc