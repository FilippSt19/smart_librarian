from fastapi.testclient import TestClient

from app.api.main import app


client = TestClient(app)


def test_chat_endpoint_exists():

    response = client.post(
        "/api/v1/chat",
        json={
            "query": "Fantasy"
        },
    )

    assert response.status_code in (
        200,
        500,
    )