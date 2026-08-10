from app.config import get_settings
from app.engine.chains.recommendation_chain import (
    RecommendationChain,
)
from app.engine.llm.openai_provider import (
    OpenAIProvider,
)
from app.engine.retrieval.rag_retriever import (
    RAGRetriever,
)
from app.engine.tools.registry import ToolRegistry
from app.engine.tools.summary_tool import SummaryTool
from app.services.content_filter_service import (
    ContentFilterService,
)


class RecommendationService:

    def __init__(
        self,
        content_filter: ContentFilterService | None = None,
    ) -> None:
        self.settings = get_settings()

        self.content_filter = (
            content_filter
            if content_filter is not None
            else ContentFilterService()
        )

        self.chain = RecommendationChain(
            retriever=RAGRetriever(),
            provider=OpenAIProvider(),
            registry=ToolRegistry(
                [
                    SummaryTool(),
                ]
            ),
            settings=self.settings,
        )

    def recommend(
        self,
        query: str,
    ) -> dict[str, str] | str:

        if (
            self.content_filter
            .contains_inappropriate_language(query)
        ):
            return (
                "Please keep the conversation respectful "
                "and try your request again."
            )

        return self.chain.run(query)