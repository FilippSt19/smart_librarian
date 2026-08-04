from fastapi import FastAPI, Request
from fastapi.responses import Response
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware


def configure_security_middleware(
    application: FastAPI,
) -> None:
    application.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=[
            "localhost",
            "127.0.0.1",
            "testserver",
        ],
    )

    application.add_middleware(
        GZipMiddleware,
        minimum_size=1000,
    )

    @application.middleware("http")
    async def add_security_headers(
        request: Request,
        call_next,
    ) -> Response:
        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"

        return response