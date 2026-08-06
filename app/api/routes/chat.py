import traceback

from fastapi import APIRouter, HTTPException, status

from app.api.schemas.chat import ChatRequest, ChatResponse
from app.engine.agents.factory import (
    AgentFactory,
)


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
        response = agent.chat(
            request.query
        )

        return ChatResponse(
            response=response
        )

    except Exception as exc:
        traceback.print_exc()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        ) from exc