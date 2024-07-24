import pytest
from fastapi import status

ENDPOINT = "/teams"


def test_get_team_not_found(client):
    # assert that a 404 is raised when child is not found
    non_existing_id = 0
    response = client.get(f"{ENDPOINT}/{non_existing_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text


@pytest.fixture(name="client")
def client_with_community_and_team(client):
    # arrange two communities
    for i in range(2):
        client.post(
            "/communities",
            json={
                "name": f"Community {i}",
            },
        )
    return client


def test_post_team_success(client):
    # test successfull creation of a team
    team_1 = "Team 1"
    data = {"community_id": 1, "name": team_1, "children": []}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED
    id_ = response.json().get("id")

    # assert that team can be obtained
    response_get = client.get(f"{ENDPOINT}/{id_}")
    assert response_get.status_code == status.HTTP_200_OK
    assert response_get.json().get("name") == team_1
    assert response_get.json().get("is_active")


def test_get_team_filter_community(client):
    # test that we can filter teams by community_id
    team_1 = "Team 1"
    data = {"community_id": 1, "name": team_1, "children": []}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED
    team_2 = "Team 2"
    data = {"community_id": 2, "name": team_2, "children": []}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED
    response_get = client.get(f"{ENDPOINT}?community_id=1")
    assert response_get.status_code == status.HTTP_200_OK
    assert len(response_get.json()) == 1
    assert response_get.json()[0].get("name") == team_1
