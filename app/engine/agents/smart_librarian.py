from app.engine.agents.base import BaseAgent
from app.services.recommendation_service import (
    RecommendationService,
)


class SmartLibrarianAgent(BaseAgent):

    def __init__(self):

        self.service = RecommendationService()

    def run(
        self,
        query: str,
    ) -> str:

        return self.chat(query)

    def chat(
        self,
        query: str,
    ) -> str:

        return self.service.recommend(
            query
        )