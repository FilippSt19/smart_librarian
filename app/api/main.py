from fastapi import FastAPI

from app.common.exception_handlers import (
    register_exception_handlers,
)
from app.api.middleware.cors import configure_cors
from app.api.middleware.security import (
    configure_security_middleware,
)
from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Smart Librarian API",
        description="AI Book Recommendation API",
        version="1.0.0",
    )

    configure_cors(app)
    configure_security_middleware(app)
    register_exception_handlers(
        app
    )

    app.include_router(
        health_router,
        prefix="/api/v1",
    )

    app.include_router(
        chat_router,
        prefix="/api/v1",
    )

    return app


app = create_app()