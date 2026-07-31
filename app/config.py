import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY nu este setată. Adaugă cheia în fișierul .env."
    )

# OpenAI Models
CHAT_MODEL = "gpt-4.1-mini"
EMBEDDING_MODEL = "text-embedding-3-small"

# ChromaDB Configuration
CHROMA_DB_PATH = "data/chroma_db"
COLLECTION_NAME = "book_summaries"