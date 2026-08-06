import traceback

from fastapi import APIRouter, HTTPException, status

from app.api.schemas.chat import ChatRequest, ChatResponse
from app.services.recommendation_service import RecommendationService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

recommendation_service = RecommendationService()


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
) -> ChatResponse:
    try:
        response = recommendation_service.recommend(
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