# Smart Librarian

Smart Librarian is an AI-powered book recommendation platform built with FastAPI, React and Streamlit.

The application combines Retrieval-Augmented Generation (RAG), semantic search using ChromaDB and OpenAI models to recommend books from natural language queries.

---

## Features

- AI-powered book recommendations
- Retrieval-Augmented Generation (RAG)
- Semantic search with ChromaDB
- OpenAI Function Calling
- FastAPI REST API
- React frontend
- Streamlit frontend
- Repository Pattern
- Service Layer
- Dependency Injection
- Docker and Docker Compose support
- GitHub Actions CI
- Unit and integration tests

---

## Project Structure

```text
smart_librarian_project/

├── app/
│   ├── api/
│   ├── common/
│   ├── config/
│   ├── engine/
│   ├── repositories/
│   ├── scripts/
│   ├── services/
│   └── tests/
│
├── frontend_react/
│
├── frontend_streamlit/
│
├── data/
│
├── compose.yaml
│
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
- Uvicorn

### Frontend

React

- React
- TypeScript
- Vite
- Axios

Streamlit

- Streamlit

### DevOps

- Docker
- Docker Compose
- Rancher Desktop
- nerdctl
- GitHub Actions

---

## Running the Application

### Recommended

The recommended way to run the project is with Docker Compose.

Build the containers:

```bash
nerdctl compose build
```

Start the complete application:

```bash
nerdctl compose up
```

This starts:

- FastAPI backend
- React frontend
- Streamlit frontend

Default URLs:

| Service | URL |
|---------|-----|
| React | http://localhost:5173 |
| Streamlit | http://localhost:8501 |
| Swagger | http://localhost:8000/docs |

---

## Local Development

### Backend

```bash
python -m uvicorn app.api.main:app --reload
```

Swagger

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

Open

```text
http://localhost:5173
```

---

### Streamlit Frontend

```bash
streamlit run frontend_streamlit/streamlit_app.py
```

Open

```text
http://localhost:8501
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/chat` | Book recommendations |
| POST | `/api/v1/ingestion/books` | Book ingestion |

---

## Running Tests

Run all tests

```bash
python -m pytest app/tests
```

Run unit tests

```bash
python -m pytest app/tests/unit
```

Run integration tests

```bash
python -m pytest app/tests/integration
```

---

## Continuous Integration

GitHub Actions automatically executes:

- Backend CI
- Frontend CI

on every push and pull request to the `main` branch.

---

## Environment Variables

Create a `.env` file in the project root.

Required variable:

```text
OPENAI_API_KEY=your_openai_api_key
```

Example configuration:

```text
CHAT_MODEL=gpt-4.1-mini
EMBEDDING_MODEL=text-embedding-3-small
DEFAULT_N_RESULTS=3
CHROMA_DB_PATH=data/chroma_db
COLLECTION_NAME=book_summaries
```

---

## Architecture

The backend follows a layered architecture:

```text
API
        │
        ▼
Services
        │
        ▼
Engine
        │
        ├── Agents
        ├── Chains
        ├── Retrieval
        ├── LLM
        └── Tools
        │
        ▼
Repositories
        │
        ▼
ChromaDB
```

The project uses:

- Repository Pattern
- Service Layer
- Factory Pattern
- Dependency Injection
- Retrieval-Augmented Generation (RAG)

---

## License

This project was developed for educational purposes.