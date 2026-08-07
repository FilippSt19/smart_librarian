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


class RecommendationService:

    def __init__(self) -> None:
        self.settings = get_settings()

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
    ) -> dict[str, str]:

        return self.chain.run(query)