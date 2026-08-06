FROM python:3.13-slim

WORKDIR /app

ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY frontend_streamlit ./frontend_streamlit
COPY data ./data

EXPOSE 8501

CMD ["streamlit", "run", "frontend_streamlit/streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]