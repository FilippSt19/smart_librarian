from pydantic import BaseModel, Field


class BookArtworkRequest(BaseModel):

    title: str = Field(
        min_length=1,
        max_length=200,
    )

    author: str = Field(
        min_length=1,
        max_length=200,
    )

    genre: str = Field(
        min_length=1,
        max_length=100,
    )

    summary: str = Field(
        min_length=1,
        max_length=4000,
    )


class BookArtworkResponse(BaseModel):

    image: str