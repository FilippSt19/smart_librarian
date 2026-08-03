"""
This module coordinates the entire book ingestion workflow.
It orchestrates data processing, validation, and storage operations.
"""
from openai import OpenAI

from app.config import OPENAI_API_KEY, CHAT_MODEL
from app.rag import RAGRetriever

class SmartLibrarian:
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.retriever = RAGRetriever()
        
    def build_context(
        self,
        documents: list[dict],
    ) -> str:
         
        context = ""

        for document in documents:

            context += (
                f"Title: {document['title']}\n"
                f"{document['document']}\n\n"
            )

        return context
    
    def chat(
        self,
        query: str,
    ) -> str:

        documents = self.retriever.retrieve(query)

        context = self.build_context(documents)

        response = self.client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful librarian."
                        "Recommend ONE book using only the provided context."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"""
Context:

{context}

User request:

{query}
"""
                    )
                }
            ]
        )

        return response.choices[0].message.content