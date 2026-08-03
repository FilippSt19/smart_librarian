from pathlib import Path

from app.embeddings import EmbeddingService
from app.vector_store import VectorStore


BOOKS_PATH = Path("data/book_summaries.txt")


def load_books() -> list[str]:
    """
    Read the book summaries file and split it into individual books.
    """

    text = BOOKS_PATH.read_text(encoding="utf-8")

    books = text.split("## Title:")

    books = [
        book.strip()
        for book in books
        if book.strip()
    ]

    return books


def main():

    books = load_books()

    embedding_service = EmbeddingService()
    vector_store = VectorStore()

    print(f"Found {len(books)} books.\n")

    for index, book in enumerate(books):

        title = book.split("\n")[0].strip()

        embedding = embedding_service.create_embedding(book)

        vector_store.add_document(
            document_id=f"book_{index + 1}",
            document=book,
            embedding=embedding,
            metadata={
                "title": title
            }
        )

        print(f"Indexed: {title}")

    print("\nIndexing completed successfully!")
    print(
        f"Total documents in ChromaDB: "
        f"{vector_store.count_documents()}"
    )


if __name__ == "__main__":
    main()