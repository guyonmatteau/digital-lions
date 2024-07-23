import pytest
from fastapi import status

ENDPOINT = "/children"


def test_get_child_not_found(client):
    # assert that a 404 is raised when child is not found
    non_existing_id = 0
    response = client.get(f"{ENDPOINT}/{non_existing_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text


def test_post_child_non_existing_team(client):
    # assert that we can't create a child for a non-existing team
    data = {"first_name": "Firstname", "last_name": "Lastname", "team_id": 0}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, repsonse.text


def test_post_child_success(client, mocker):
    # test successfull creation of a child
    post_community = client.post(
        "/communities",
        json={
            "name": "Community 1",
        },
    )
    assert post_community.status_code == status.HTTP_201_CREATED, post_community.text
    team_community = client.post(
        "/teams",
        json={"name": "Team 1", "community_id": 1, "children": []},
    )
    assert team_community.status_code == status.HTTP_201_CREATED, team_community.text
    child_name = "Firstname"
    data = {"first_name": child_name, "last_name": "Lastname", "team_id": 1}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED, response.text
    id_ = response.json().get("id")

    # test that child can be obtained
    response_get = client.get(f"{ENDPOINT}/{id_}")
    assert response_get.status_code == status.HTTP_200_OK, response_get.text
    assert response_get.json().get("first_name") == child_name
