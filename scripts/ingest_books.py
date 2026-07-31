from pathlib import Path

BOOKS_PATH = Path("data/book_summaries.txt")

text = BOOKS_PATH.read_text(encoding="utf-8")

books = text.split("## Title:")

books = [book.strip() for book in books if book.strip()]

from app.embeddings import EmbeddingService

embedding_service = EmbeddingService()

embedding = embedding_service.create_embedding(books[0])

print(type(embedding))
print(len(embedding))
print(embedding[:5])

print(len(books))
print(books[0][:200])