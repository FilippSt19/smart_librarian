from fastapi import FastAPI

from api.schemas import ChatRequest, ChatResponse
from app.chatbot import SmartLibrarian

app = FastAPI(
    title="Smart Librarian API",
    description="AI Book Recommendation API",
    version="1.0.0",
)

chatbot = SmartLibrarian()

@app.get("/")
def root():

    return {
        "message": "Smart Librarian API is running!"
    }
    
@app.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
):

    response = chatbot.chat(
        request.query
    )

    return ChatResponse(
        response=response
    )