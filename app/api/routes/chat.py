from fastapi import APIRouter, HTTPException, status

from app.api.schemas.chat import ChatRequest, ChatResponse
from app.engine.agents.smart_librarian import (
    SmartLibrarianAgent,
)


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

chatbot = SmartLibrarianAgent()


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(request: ChatRequest) -> ChatResponse:
    try:
        response = chatbot.chat(request.query)

        return ChatResponse(response=response)

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate recommendation.",
        ) from exc