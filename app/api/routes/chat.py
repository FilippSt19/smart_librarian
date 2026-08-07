from fastapi import APIRouter, HTTPException, status

from app.api.schemas.chat import (
    BookRecommendation,
    ChatRequest,
    ChatResponse,
)
from app.engine.agents.factory import AgentFactory


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

agent = AgentFactory.create()


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
) -> ChatResponse:

    try:
        recommendation = agent.chat(
            request.query
        )

        return ChatResponse(
            recommendation=BookRecommendation(
                **recommendation
            )
        )

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate recommendation.",
        ) from exc