from fastapi import status


def test_get_health(client):
    # basic health endpoint test
    response = client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("status") == "ok"
