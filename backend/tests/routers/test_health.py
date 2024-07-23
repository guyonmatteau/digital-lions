def test_get_health(client):
    # basic health endpoint test
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json().get("status") == "ok"
