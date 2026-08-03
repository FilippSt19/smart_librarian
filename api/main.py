from fastapi import FastAPI

app = FastAPI(
    title="Smart Librarian API",
    version="1.0.0",
)

@app.get("/")
def home():

    return {
        "message": "Smart Librarian API is running."
    }