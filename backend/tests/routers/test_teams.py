import pytest
from fastapi import status

ENDPOINT = "/teams"


def test_get_team_not_found(client):
    # assert that a 404 is raised when child is not found
    non_existing_id = 0
    response = client.get(f"{ENDPOINT}/{non_existing_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text


@pytest.fixture(name="client")
def client_with_communities(client):
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


def test_get_team_by_id(client):
    # test that we can get a team by id
    team_x = "Team X"
    children = [
        {"first_name": "Child 1", "last_name": "Last name", "age": 10},
        {"first_name": "Child 2", "last_name": "Last name", "dob": "2001-01-01"},
    ]
    data = {"community_id": 1, "name": team_x, "children": children}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED
    id_ = response.json().get("id")
    response_get = client.get(f"{ENDPOINT}/{id_}")
    assert response_get.json().get("name") == team_x


def test_delete_team_with_children(client):
    # test that we can't delete a team with children if cascade is not set
    team_x = "Team Y"
    children = [
        {"first_name": "Child 1", "last_name": "Last name", "age": 10},
        {"first_name": "Child 2", "last_name": "Last name", "dob": "2001-01-01"},
    ]
    data = {"community_id": 1, "name": team_x, "children": children}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED
    id_ = response.json().get("id")

    # assert team cannot be deleted
    response_delete = client.delete(f"{ENDPOINT}/{id_}")
    assert response_delete.status_code == status.HTTP_409_CONFLICT, response_delete.text


def test_delete_team_with_children_cascade(client):
    # test that we can't delete a team with children if cascade is not set
    team_x = "Team Y"
    children = [
        {"first_name": "Child 1", "last_name": "Last name", "age": 10},
        {"first_name": "Child 2", "last_name": "Last name", "dob": "2001-01-01"},
    ]
    data = {"community_id": 1, "name": team_x, "children": children}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == status.HTTP_201_CREATED
    id_ = response.json().get("id")

    team = client.get(f"{ENDPOINT}/{id_}")
    child_id_0 = team.json().get("children")[0].get("id")

    # assert team cannot be deleted
    response_delete = client.delete(f"{ENDPOINT}/{id_}", params={"cascade": True})
    assert response_delete.status_code == status.HTTP_200_OK, response_delete.text

    # assert that team and child have been deleted
    assert (
        client.get(f"/children/{child_id_0}").status_code == status.HTTP_404_NOT_FOUND
    )
    assert client.get(f"{ENDPOINT}/{id_}").status_code == status.HTTP_404_NOT_FOUND


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


def test_add_workshop_with_attendance(client_with_team):
    # test that we can add a workshop to a team
    team_id = 1
    attendance = [
        {"attendance": "present", "child_id": 1},
        {"attendance": "absent", "child_id": 2},
    ]
    payload = {
        "date": "2021-01-01",
        "workshop_number": 1,
        "attendance": attendance,
    }

    # assert that team progress is 0 at first
    response_team = client_with_team.get(f"{ENDPOINT}/{team_id}")
    assert response_team.json().get("program").get("progress").get("current") == 0

    response = client_with_team.post(f"{ENDPOINT}/{team_id}/workshops", json=payload)
    assert response.status_code == status.HTTP_201_CREATED, response.text

    # assert that team progress is updated
    response_team = client_with_team.get(f"{ENDPOINT}/{team_id}")
    assert response_team.json().get("program").get("progress").get("current") == 1

    response_workshop = client_with_team.get(f"{ENDPOINT}/{team_id}/workshops")
    assert response_workshop.json()[0].get("workshop").get("number") == 1


def test_add_workshop_missing_child_id(client_with_team):
    # test that we get a bad request when we are missing children
    team_id = 1
    attendance = [{"attendance": "present", "child_id": 1}]
    response = client_with_team.post(
        f"{ENDPOINT}/{team_id}/workshops",
        json={
            "workshop_number": 1,
            "date": "2021-01-01",
            "attendance": attendance,
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.text


def test_add_workshop_incorrect_child_id(client_with_team):
    # test that we get a bad request when we have extra children
    team_id = 1
    attendance = [
        {"attendance": "present", "child_id": 1},
        {"attendance": "cancelled", "child_id": 2},
        {"attendance": "present", "child_id": 3},
    ]
    response = client_with_team.post(
        f"{ENDPOINT}/{team_id}/workshops",
        json={
            "date": "2021-01-01",
            "workshop_number": 1,
            "attendance": attendance,
        },
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.text


def test_workshop_invalid_number(client_with_team):
    # assert that only a workshop can be added between 1 and 12
    team_id = 1
    attendance = [
        {"attendance": "present", "child_id": 1},
        {"attendance": "cancelled", "child_id": 2},
    ]
    response = client_with_team.post(
        f"{ENDPOINT}/{team_id}/workshops",
        json={
            "workshop_number": 0,
            "date": "2021-01-01",
            "attendance": attendance,
        },
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text


def test_workshop_already_exists(client_with_team):
    # given a workshop has been created with a number,
    # assert that the workshop cannot be created again
    team_id = 1
    attendance = [
        {"attendance": "present", "child_id": 1},
        {"attendance": "absent", "child_id": 2},
    ]
    payload = {
        "date": "2021-01-01",
        "workshop_number": 1,
        "attendance": attendance,
    }

    response = client_with_team.post(
        f"{ENDPOINT}/{team_id}/workshops",
        json=payload,
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    response = client_with_team.post(
        f"{ENDPOINT}/{team_id}/workshops",
        json=payload,
    )
    assert response.status_code == status.HTTP_409_CONFLICT, response.text


def test_workshop_number_not_subsequent(client_with_team):
    # given a team has done a workshop, assert that the next workshop added
    # can only have the workshop number of the last + 1
    team_id = 1
    attendance = [
        {"attendance": "present", "child_id": 1},
        {"attendance": "absent", "child_id": 2},
    ]

    # create workshop number 1
    response = client_with_team.post(
        f"{ENDPOINT}/{team_id}/workshops",
        json={
            "date": "2021-01-01",
            "workshop_number": 1,
            "attendance": attendance,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text

    # try to create workshop 3, which should fail
    response_post_second_workshop = client_with_team.post(
        f"{ENDPOINT}/{team_id}/workshops",
        json={
            "date": "2021-01-01",
            "workshop_number": 1 + 2,
            "attendance": attendance,
        },
    )
    assert (
        response_post_second_workshop.status_code == status.HTTP_400_BAD_REQUEST
    ), response_post_second_workshop.text


def test_team_non_active_after_completed_program(client_with_team):
    # given a team has completed all workshops, assert that the team is non-active
    pass
