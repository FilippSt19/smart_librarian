# Smart Librarian

Smart Librarian is an AI-powered book recommendation platform built with FastAPI, React, Streamlit, OpenAI, and ChromaDB.

The application combines Retrieval-Augmented Generation (RAG), semantic search, OpenAI Function Calling, conversational intent routing, and multimodal features to recommend books from natural-language queries.

Users can describe genres, themes, moods, or interests and receive a structured book recommendation together with an explanation and complete summary.

---

## Features

### AI and RAG

- AI-powered book recommendations
- Retrieval-Augmented Generation (RAG)
- Semantic search with ChromaDB
- OpenAI embeddings
- OpenAI Function Calling
- `get_summary_by_title` tool
- Structured recommendation responses
- Conversational intent classification
- Off-topic request handling
- Inappropriate-language filtering

### Multimodal Features

- Text-to-Speech for book summaries
- Speech-to-Text voice input
- AI-generated book artwork
- On-demand artwork generation

### React User Experience

- Modern responsive chat interface
- Persistent conversation history
- New conversation support
- Conversation deletion
- Scrollable conversation history
- Suggested prompts
- Recommendation cards
- Loading and typing indicators
- Responsive desktop, tablet, and mobile layouts

### Backend and Architecture

- FastAPI REST API
- React frontend
- Streamlit alternative frontend
- Repository Pattern
- Service Layer
- Factory Pattern
- Dependency Injection
- Tool Registry
- Configurable application settings
- Docker and Docker Compose support
- GitHub Actions CI
- Unit and integration tests

---

## How It Works

A typical recommendation request follows this flow:

```text
User Query
    |
    v
Content Filter
    |
    v
Intent Classification
    |
    +---- Conversation / Off-topic
    |           |
    |           v
    |     Conversational Response
    |
    +---- Book Request
                |
                v
          RAG Retrieval
                |
                v
            ChromaDB
                |
                v
        OpenAI Recommendation
                |
                v
      get_summary_by_title
          Function Call
                |
                v
          Summary Tool
                |
                v
       Structured Response
                |
                v
       React / Streamlit UI
```

For book requests, the application retrieves relevant books from the vector database before generating the recommendation.

The recommendation flow then uses the `get_summary_by_title` tool to retrieve the complete summary for the selected title.

---

## Project Structure

```text
smart_librarian_project/
|
├── app/
│   ├── api/
│   │   ├── middleware/
│   │   ├── routes/
│   │   └── schemas/
│   ├── common/
│   ├── config/
│   ├── engine/
│   │   ├── agents/
│   │   ├── chains/
│   │   ├── llm/
│   │   ├── prompts/
│   │   ├── retrieval/
│   │   └── tools/
│   ├── repositories/
│   ├── scripts/
│   ├── services/
│   └── tests/
│       ├── integration/
│       └── unit/
│
├── frontend_react/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── shared/
│   │   ├── styles/
│   │   └── types/
│   └── Dockerfile
│
├── frontend_streamlit/
│   ├── streamlit_app.py
│   └── Dockerfile
│
├── data/
│
├── .github/
│   └── workflows/
│
├── compose.yaml
└── README.md
```

---

## Technology Stack

### Backend

- Python 3.13
- FastAPI
- OpenAI API
- ChromaDB
- Pydantic
- pydantic-settings
- Uvicorn
- pytest

### React Frontend

- React
- TypeScript
- Vite
- Axios
- React Icons

### Alternative Frontend

- Streamlit

### AI

- OpenAI chat models
- OpenAI embeddings
- OpenAI image generation
- Retrieval-Augmented Generation
- Function Calling / Tools

### DevOps

- Docker
- Docker Compose
- Rancher Desktop
- containerd
- nerdctl
- GitHub Actions
- GitHub Pages

---

## Running the Application

### Recommended: Docker Compose

The recommended way to run the complete application locally is with Docker Compose.

Build the containers:

```bash
nerdctl compose build
```

Start the application:

```bash
nerdctl compose up
```

This starts:

- FastAPI backend
- React frontend
- Streamlit frontend

### Default URLs

| Service | URL |
| --- | --- |
| React | http://localhost:5173 |
| Streamlit | http://localhost:8501 |
| FastAPI | http://localhost:8000 |
| Swagger | http://localhost:8000/docs |

---

## Local Development

### Backend

From the project root:

```bash
python -m uvicorn app.api.main:app --reload
```

API documentation:

```text
http://localhost:8000/docs
```

---

### React Frontend

```bash
cd frontend_react
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

Production build:

```bash
npm run build
```

---

### Streamlit Frontend

From the project root:

```bash
streamlit run frontend_streamlit/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/chat` | Chat and book recommendations |
| POST | `/api/v1/ingestion/books` | Ingest books into the vector store |
| POST | `/api/v1/images/book-artwork` | Generate AI artwork for a recommended book |

Interactive API documentation is available through Swagger at:

```text
http://localhost:8000/docs
```

---

## Recommendation Response

Book requests return structured recommendation data:

```json
{
  "recommendation": {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "genre": "Romance",
    "reason": "Why this book matches the user's request.",
    "summary": "Complete book summary."
  },
  "message": null
}
```

Conversational and off-topic requests can return a normal assistant message instead:

```json
{
  "recommendation": null,
  "message": "I specialize in books and book recommendations."
}
```

---

## Conversation Routing

Smart Librarian distinguishes between different types of user requests.

### Book Request

Examples:

```text
Recommend me a fantasy book about friendship.
I want something about freedom and surveillance.
What is The Hobbit about?
```

These requests use the RAG and Function Calling pipeline.

### Conversation

Examples:

```text
Hey
Thanks
What can you do?
```

These receive a normal conversational response.

### Off-topic Request

Examples:

```text
Give me a pizza recipe.
Write Python code for me.
```

Smart Librarian stays within its book-focused domain and can redirect the user toward relevant books instead.

---

## Conversation History

The React frontend supports persistent conversation history.

Conversation data is stored locally in the browser using `localStorage`.

Features include:

- multiple conversations
- persistent history after refresh
- conversation switching
- conversation deletion
- scrollable history
- automatic conversation titles
- prevention of empty history entries

Conversation history is browser-local and is not synchronized between devices.

---

## Voice Features

### Text-to-Speech

Book summaries can be read aloud directly from the recommendation card using the browser Speech Synthesis API.

### Speech-to-Text

Users can dictate book requests using the microphone button in the React chat input.

Speech recognition availability depends on browser support.

---

## AI Artwork Generation

Recommended books can optionally generate an original AI illustration.

Artwork generation:

- is triggered manually by the user
- runs through the FastAPI backend
- keeps the OpenAI API key server-side
- does not attempt to reproduce existing book covers
- generates artwork based on the book's title, genre, and summary

Generated images are not permanently stored by the application.

---

## Content Filtering

Smart Librarian includes an inappropriate-language filter.

Blocked messages are intercepted before entering the recommendation pipeline and receive a polite response instead of being sent through the RAG recommendation flow.

---

## Running Tests

Run the complete test suite:

```bash
python -m pytest
```

Run unit tests:

```bash
python -m pytest app/tests/unit
```

Run integration tests:

```bash
python -m pytest app/tests/integration
```

---

## Continuous Integration

GitHub Actions runs automated CI workflows for the backend and frontend.

The CI pipeline validates:

- Python tests
- backend dependencies
- TypeScript compilation
- React production build

Workflows run on pushes and pull requests to the `main` branch.

---

## GitHub Pages

The React frontend can be deployed through GitHub Pages.

The Vite project is configured with:

```ts
base: "/smart_librarian/"
```

GitHub Pages hosts only the static React frontend.

The FastAPI backend, ChromaDB, and OpenAI integration require a separately deployed backend service for the complete application to work publicly.

---

## Environment Variables

Create a `.env` file in the project root.

Required:

```env
OPENAI_API_KEY=your_openai_api_key
```

Example configuration:

```env
CHAT_MODEL=gpt-4.1-mini
EMBEDDING_MODEL=text-embedding-3-small
IMAGE_MODEL=gpt-image-2

DEFAULT_N_RESULTS=3

CHROMA_DB_PATH=data/chroma_db
COLLECTION_NAME=book_summaries

CORS_ORIGINS=http://localhost:5173
ALLOWED_HOSTS=localhost;127.0.0.1
```

Do not expose `OPENAI_API_KEY` through frontend environment variables.

---

## Architecture

The backend follows a layered architecture:

```text
API Layer
    |
    v
Service Layer
    |
    v
Engine
    |
    +-- Agents
    +-- Chains
    +-- LLM Provider
    +-- Prompts
    +-- Retrieval
    +-- Tools
    |
    v
Repository Layer
    |
    v
ChromaDB
```

The project uses:

- Repository Pattern
- Service Layer
- Factory Pattern
- Dependency Injection
- Tool Registry
- Retrieval-Augmented Generation
- OpenAI Function Calling

---

## Current Limitations

- The current book knowledge base is intentionally small and can be expanded with a larger dataset.
- Conversation history is stored locally in the browser rather than in a server-side database.
- Speech-to-Text depends on browser support.
- GitHub Pages hosts only the React frontend; the FastAPI backend requires separate hosting.
- AI artwork generation requires an active OpenAI API connection.

---

## Future Improvements

Potential extensions include:

- saved/favorite books
- recommendation alternatives
- conversation history search
- clear-history controls
- recommendation copy/share actions
- dark mode
- larger book dataset
- server-side conversation persistence
- public backend deployment

---

## License

This project was developed for educational purposes.