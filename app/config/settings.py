from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # OpenAI
    openai_api_key: str
    chat_model: str = "gpt-4.1-mini"
    embedding_model: str = "text-embedding-3-small"

    # ChromaDB
    chroma_db_path: str = "data/chroma_db"
    collection_name: str = "book_summaries"

    # Files
    book_summaries_path: str = "data/book_summaries.txt"
    summaries_json_path: str = "data/summaries.json"

    # RAG
    default_n_results: int = 3
    temperature: float = 0.3

    # API
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    debug: bool = True

    # CORS / Security
    cors_origins_raw: str = Field(
        default="http://localhost:5173",
        alias="CORS_ORIGINS",
    )
    allowed_hosts_raw: str = Field(
        default="localhost;127.0.0.1;testserver",
        alias="ALLOWED_HOSTS",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def cors_origins(self) -> list[str]:
        return self._split_values(self.cors_origins_raw)

    @property
    def allowed_hosts(self) -> list[str]:
        return self._split_values(self.allowed_hosts_raw)

    @staticmethod
    def _split_values(raw_value: str) -> list[str]:
        return [
            value.strip()
            for value in raw_value.split(";")
            if value.strip()
        ]


@lru_cache
def get_settings() -> Settings:
    return Settings()
