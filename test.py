from app.rag import RAGRetriever

retriever = RAGRetriever()

results = retriever.retrieve(
    "I want a book about friendship and magic."
)

for index, result in enumerate(results, start=1):

    print("=" * 70)
    print(f"Result {index}")
    print("=" * 70)

    print(f"Title: {result['title']}\n")

    print(result["document"][:400])

    print()