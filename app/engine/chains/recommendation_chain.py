import json
from pathlib import Path

from app.engine.prompts.loader import PromptLoader


SYSTEM_PROMPT = PromptLoader.load(
    Path(
        "app/engine/prompts/smart_librarian_system.md"
    )
)

INTENT_PROMPT = PromptLoader.load(
    Path(
        "app/engine/prompts/intent_classifier.md"
    )
)

CONVERSATION_PROMPT = PromptLoader.load(
    Path(
        "app/engine/prompts/conversation.md"
    )
)


class RecommendationChain:

    def __init__(
        self,
        retriever,
        provider,
        registry,
        settings,
    ):
        self.retriever = retriever
        self.provider = provider
        self.registry = registry
        self.settings = settings

    def classify_intent(
        self,
        query: str,
    ) -> str:

        response = self.provider.generate(
            prompt=query,
            system_prompt=INTENT_PROMPT,
            temperature=0,
        )

        try:
            result = json.loads(response)
        except json.JSONDecodeError:
            return "book"

        intent = result.get("intent")

        if intent == "conversation":
            return "conversation"

        return "book"

    def respond_to_conversation(
        self,
        query: str,
    ) -> str:

        return self.provider.generate(
            prompt=query,
            system_prompt=CONVERSATION_PROMPT,
            temperature=0.3,
        )

    def build_context(
        self,
        documents: list[dict],
    ) -> str:

        context = []

        for document in documents:
            context.append(
                (
                    f"Title: {document['title']}\n"
                    f"{document['document']}"
                )
            )

        return "\n\n".join(context)

    @staticmethod
    def _parse_recommendation(
        content: str | None,
    ) -> dict[str, str]:

        if not content:
            raise ValueError(
                "No recommendation generated."
            )

        try:
            recommendation = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError(
                "Model returned invalid JSON."
            ) from exc

        required_fields = {
            "title",
            "author",
            "genre",
            "reason",
            "summary",
        }

        missing_fields = (
            required_fields
            - recommendation.keys()
        )

        if missing_fields:
            raise ValueError(
                "Missing recommendation fields: "
                + ", ".join(sorted(missing_fields))
            )

        return {
            "title": str(
                recommendation["title"]
            ),
            "author": str(
                recommendation["author"]
            ),
            "genre": str(
                recommendation["genre"]
            ),
            "reason": str(
                recommendation["reason"]
            ),
            "summary": str(
                recommendation["summary"]
            ),
        }

    def run(
        self,
        query: str,
    ) -> dict[str, str] | str:

        intent = self.classify_intent(
            query
        )

        if intent == "conversation":
            return self.respond_to_conversation(
                query
            )

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
                "content": (
                    "Context:\n\n"
                    f"{context}\n\n"
                    "User request:\n\n"
                    f"{query}"
                ),
            },
        ]

        response = (
            self.provider.client
            .chat.completions.create(
                model=self.settings.chat_model,
                temperature=self.settings.temperature,
                messages=messages,
                tools=self.registry.schemas(),
                tool_choice="auto",
            )
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return self._parse_recommendation(
                message.content
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
            self.provider.client
            .chat.completions.create(
                model=self.settings.chat_model,
                temperature=self.settings.temperature,
                messages=messages,
            )
        )

        final_content = (
            final_response
            .choices[0]
            .message
            .content
        )

        return self._parse_recommendation(
            final_content
        )