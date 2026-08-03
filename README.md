# 📚 Smart Librarian

An AI-powered book recommendation system built with **Python**, **OpenAI GPT**, **RAG (Retrieval-Augmented Generation)** and **ChromaDB**.

The application recommends books based on the user's interests using semantic search and enriches the recommendation with a complete book summary through **OpenAI Function Calling**.

---

# 🚀 Features

- 📚 AI book recommendations
- 🔍 Semantic search using ChromaDB
- 🧠 OpenAI Embeddings (`text-embedding-3-small`)
- 🤖 OpenAI GPT (`gpt-4.1-mini`)
- ⚡ Retrieval-Augmented Generation (RAG)
- 🛠 OpenAI Function Calling
- 📖 Local JSON knowledge base
- 💬 Streamlit chat interface

---

# 🏗 Architecture

```
User
 │
 ▼
Streamlit UI
 │
 ▼
SmartLibrarian
 │
 ├───────────────┐
 │               │
 ▼               ▼
RAG          Function Calling
 │               │
 ▼               ▼
ChromaDB    summaries.json
 │
 ▼
OpenAI Embeddings
 │
 ▼
OpenAI GPT
```

---

# 📂 Project Structure

```
smart_librarian_project/

│
├── app/
│   ├── chatbot.py
│   ├── config.py
│   ├── embeddings.py
│   ├── prompts.py
│   ├── rag.py
│   ├── tools.py
│   └── vector_store.py
│
├── data/
│   ├── book_summaries.txt
│   ├── summaries.json
│   └── chroma_db/
│
├── scripts/
│   └── ingest_books.py
│
├── ui/
│   └── streamlit_app.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Technologies

- Python 3.13
- OpenAI API
- GPT-4.1-mini
- text-embedding-3-small
- ChromaDB
- Streamlit
- python-dotenv

---

# 🔄 Application Flow

## 1. Data Ingestion

```
book_summaries.txt

↓

OpenAI Embeddings

↓

ChromaDB
```

The ingestion pipeline reads all book summaries, generates embeddings and stores them in ChromaDB.

---

## 2. Retrieval

```
User Query

↓

Embedding

↓

ChromaDB

↓

Top 3 Relevant Books
```

The system performs semantic search instead of keyword matching.

---

## 3. Generation

```
Retrieved Context

↓

GPT

↓

Book Recommendation
```

GPT recommends exactly one book using the retrieved context.

---

## 4. Function Calling

```
GPT

↓

get_summary_by_title()

↓

summaries.json

↓

Complete Summary

↓

Final Response
```

After recommending a book, GPT automatically calls a local Python tool to retrieve the complete summary.

---

# 📸 Streamlit Interface

The Streamlit interface allows users to:

- Ask for recommendations
- Receive AI-generated responses
- Keep conversation history
- Explore example prompts

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/smart_librarian.git

cd smart_librarian
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.\.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```text
OPENAI_API_KEY=your_api_key
```

---

# ▶️ Run the ingestion pipeline

```bash
python -m scripts.ingest_books
```

---

# ▶️ Run Streamlit

```bash
streamlit run ui/streamlit_app.py
```

---

# 💬 Example Questions

- I want a fantasy book about friendship.
- Recommend a romance novel.
- Suggest a dystopian novel.
- I love war stories.
- Recommend a science fiction novel.
- Give me something similar to Harry Potter.

---

# 🧠 What I Learned

During this project I implemented:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- OpenAI Embeddings
- OpenAI Function Calling
- ChromaDB
- Streamlit
- Project architecture and modular design
- Configuration management
- Git workflow with incremental commits

---

# 🔮 Future Improvements

- ✅ FastAPI Backend
- ✅ React Frontend
- ✅ GitHub Actions
- ✅ Docker Support
- ✅ Voice Mode (Speech-to-Text)
- ✅ Text-to-Speech
- ✅ AI Image Generation
- ✅ Content Moderation

---

# 👨‍💻 Author

Filip Stanciu

Junior Data Engineer / AI Engineer

Endava