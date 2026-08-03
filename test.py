from app.rag import RAGRetriever

retriever = RAGRetriever()

results = retriever.retrieve(
    "I want a book about friendship and magic."
)

print(results)