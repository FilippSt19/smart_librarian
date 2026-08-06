from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)


def test_ingestion_endpoint_exists():

    response = client.post("/api/v1/ingestion/books")

    print(response.status_code)
    print(response.text)

    assert response.status_code != 404