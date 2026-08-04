from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.common.exceptions import (
    SmartLibrarianError,
)


def register_exception_handlers(
    app: FastAPI,
) -> None:

    @app.exception_handler(
        SmartLibrarianError
    )
    async def handle_custom_exception(
        request,
        exc,
    ):

        return JSONResponse(
            status_code=500,
            content={
                "detail": str(exc),
            },
        )