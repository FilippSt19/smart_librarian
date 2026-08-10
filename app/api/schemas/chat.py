from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    query: str = Field(
        min_length=1,
        max_length=1000,
    )


class BookRecommendation(BaseModel):

    title: str
    author: str
    genre: str
    reason: str
    summary: str


class ChatResponse(BaseModel):

    recommendation: BookRecommendation | None = None
    message: str | None = None