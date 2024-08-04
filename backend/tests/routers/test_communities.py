import pytest
from fastapi import status

ENDPOINT = "/communities"


def test_get_community_not_found(client):
    # assert that a 404 is raised when community is not found
    non_existing_id = 0
    response = client.get(f"{ENDPOINT}/{non_existing_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_post_community_success(client):
    # test successfull creation of a community
    community_name = "Community 1"
    data = {"name": community_name}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED
    id_ = response.json().get("id")

    # test that community can be obtained
    response_get = client.get(f"{ENDPOINT}/{id_}")
    assert response_get.status_code == status.HTTP_200_OK
    assert response_get.json().get("name") == community_name
    assert response_get.json().get("is_active")


def test_post_community_duplicate(client):
    # test that we can't create the same community twice
    data = {"name": "Community 2"}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED

    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_409_CONFLICT


def test_patch_community_success(client):
    # assert that a community can be updated
    data = {"name": "Community 3"}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED
    id_ = response.json().get("id")

    data = {"is_active": False}
    response_patch = client.patch(f"{ENDPOINT}/{id_}", json=data)
    assert response_patch.status_code == status.HTTP_200_OK

    # check new status
    response_get_json = client.get(f"{ENDPOINT}/{id_}").json()
    assert not response_get_json.get("is_active")
    assert response_get_json.get("last_updated_at") != response_get_json.get(
        "created_at"
    )


def test_patch_community_not_found(client):
    # test that we can't update a non-existing community
    non_existing_id = 100
    data = {"is": "Community 3"}
    response = client.patch(f"{ENDPOINT}/{non_existing_id}", json=data)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.fixture(name="client_with_team")
def client_with_community_and_team(client):
    # arrange two communities
    children = [
        {"first_name": "Child 1", "last_name": "Last name", "age": 10},
        {"first_name": "Child 2", "last_name": "Last name", "dob": "2001-01-01"},
    ]

    client.post(
        "/communities",
        json={"name": "Community 1"},
    )
    client.post(
        "/teams", json={"community_id": 1, "name": "Team 1", "children": children}
    )
    client.post(
        "/teams", json={"community_id": 1, "name": "Team 2", "children": children}
    )
    return client


def test_delete_community_with_teams_error(client_with_team):
    # test that we can't delete a community with teams
    community_id = client_with_team.get(ENDPOINT).json()[0].get("id")
    response = client_with_team.delete(f"{ENDPOINT}/{community_id}")
    assert response.status_code == status.HTTP_409_CONFLICT, response.text


def test_delete_community_with_teams_success(client_with_team):
    # test that we can delete a community with teams when cascading
    community_id = client_with_team.get(ENDPOINT).json()[0].get("id")
    response = client_with_team.delete(
        f"{ENDPOINT}/{community_id}", params={"cascade": True}
    )
    assert response.status_code == status.HTTP_200_OK, response.text
