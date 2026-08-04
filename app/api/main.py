from fastapi import FastAPI

from app.api.middleware.cors import configure_cors
from app.api.middleware.security import configure_security
from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router


def create_app() -> FastAPI:
    application = FastAPI(
        title="Smart Librarian API",
        description="AI Book Recommendation API",
        version="1.0.0",
    )

    configure_cors(application)
    configure_security(application)

    application.include_router(health_router)
    application.include_router(chat_router)

    return application


app = create_app()