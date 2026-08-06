from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Smart Librarian API is running"
    }


@router.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok"
    }