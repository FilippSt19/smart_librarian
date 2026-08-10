from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from app.api.schemas.image import (
    BookArtworkRequest,
    BookArtworkResponse,
)
from app.services.image_generation_service import (
    ImageGenerationService,
)


router = APIRouter(
    prefix="/images",
    tags=["Images"],
)

image_generation_service = (
    ImageGenerationService()
)


@router.post(
    "/book-artwork",
    response_model=BookArtworkResponse,
)
def generate_book_artwork(
    request: BookArtworkRequest,
) -> BookArtworkResponse:

    try:
        image = (
            image_generation_service
            .generate_book_artwork(
                title=request.title,
                author=request.author,
                genre=request.genre,
                summary=request.summary,
            )
        )

        return BookArtworkResponse(
            image=image,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=(
                status.HTTP_500_INTERNAL_SERVER_ERROR
            ),
            detail=(
                "Failed to generate book artwork."
            ),
        ) from exc