import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Application configuration.
    """

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY nu este setată. Adaugă cheia în fișierul .env."
        )

    CHAT_MODEL = "gpt-4.1-mini"
    EMBEDDING_MODEL = "text-embedding-3-small"

    # ChromaDB
    CHROMA_DB_PATH = "data/chroma_db"
    COLLECTION_NAME = "book_summaries"
    DEFAULT_N_RESULTS = 10
    TEMPERATURE = 0.7
    
    CORS_ORIGINS_RAW = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173"
    )
    
    CORS_ORIGINS = [
        origin.strip()
        for origin in CORS_ORIGINS_RAW.split(";")
        if origin.strip()
    ]