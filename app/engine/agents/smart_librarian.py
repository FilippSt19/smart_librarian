from app.engine.agents.base import BaseAgent
from app.services.recommendation_service import (
    RecommendationService,
)


class SmartLibrarianAgent(BaseAgent):

    def __init__(self) -> None:
        self.service = RecommendationService()

    def run(
        self,
        query: str,
    ) -> dict[str, str] | str:
        return self.chat(query)

    def chat(
        self,
        query: str,
    ) -> dict[str, str] | str:
        return self.service.recommend(query)