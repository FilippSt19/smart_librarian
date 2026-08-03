from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.schemas import ChatRequest, ChatResponse
from app.chatbot import SmartLibrarian

app = FastAPI(
    title="Smart Librarian API",
    description="AI Book Recommendation API",
    version="1.0.0",
)

# CORS
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
def chat(request: ChatRequest):

    response = chatbot.chat(request.query)

    return ChatResponse(
        response=response
    )