from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import Config


def configure_cors(
    application: FastAPI,
) -> None:

    application.add_middleware(
        CORSMiddleware,

        allow_origins=Config.CORS_ORIGINS,

        allow_credentials=True,

        allow_methods=[
            "GET",
            "POST",
            "OPTIONS",
        ],

        allow_headers=[
            "Content-Type",
            "Authorization",
        ],
    )