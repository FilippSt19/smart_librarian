import json
from pathlib import Path

from app.config import get_settings
from app.engine.llm.openai_provider import OpenAIProvider
from app.engine.prompts.loader import PromptLoader
from app.engine.retrieval.rag_retriever import RAGRetriever
from app.engine.tools.registry import ToolRegistry
from app.engine.tools.summary_tool import SummaryTool


SYSTEM_PROMPT = PromptLoader.load(
    Path(
        "app/engine/prompts/smart_librarian_system.md"
    )
)


class RecommendationService:

    def __init__(self):

        self.settings = get_settings()

        self.provider = OpenAIProvider()

        self.retriever = RAGRetriever()

        self.registry = ToolRegistry(
            [
                SummaryTool(),
            ]
        )

    def build_context(
        self,
        documents: list[dict],
    ) -> str:

        context = []

        for document in documents:

            context.append(
                f"Title: {document['title']}\n"
                f"{document['document']}"
            )

        return "\n\n".join(context)

    def recommend(
        self,
        query: str,
    ) -> str:

        documents = self.retriever.retrieve(
            query=query,
            n_results=self.settings.default_n_results,
        )

        context = self.build_context(
            documents
        )

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"""
Context:

{context}

User request:

{query}
""",
            },
        ]

        response = (
            self.provider.client.chat.completions.create(
                model=self.settings.chat_model,
                temperature=self.settings.temperature,
                messages=messages,
                tools=self.registry.schemas(),
                tool_choice="auto",
            )
        )

        message = response.choices[0].message

        if not message.tool_calls:

            return (
                message.content
                or "No response generated."
            )

        tool_call = message.tool_calls[0]

        arguments = json.loads(
            tool_call.function.arguments
        )

        tool_result = self.registry.execute(
            tool_call.function.name,
            arguments,
        )

        messages.append(message)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": tool_result,
            }
        )

        final_response = (
            self.provider.client.chat.completions.create(
                model=self.settings.chat_model,
                temperature=self.settings.temperature,
                messages=messages,
            )
        )

        return (
            final_response
            .choices[0]
            .message
            .content
            or "No response generated."
        )