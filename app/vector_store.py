import chromadb

from app.config import CHROMA_DB_PATH, COLLECTION_NAME


class VectorStore:
    def __init__(self):
        
        """
        Initialize the ChromaDB client and collection.
        """

        self.client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )