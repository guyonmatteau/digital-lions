ENDPOINT = "/communities"


def test_get_community_not_found(client):
    # assert that a 404 is raised when community is not found
    non_existing_id = 0
    response = client.get(f"{ENDPOINT}/{non_existing_id}")
    assert response.status_code == 404


def test_post_community_success(client):
    # test successfull creation of a community
    community_name = "Community 1"
    data = {"name": community_name}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == 201
    id_ = response.json().get("id")

    # test that community can be obtained
    response_get = client.get(f"{ENDPOINT}/{id_}")
    assert response_get.status_code == 200
    assert response_get.json().get("name") == community_name
    assert response_get.json().get("is_active")


def test_post_community_duplicate(client):
    # test that we can't create the same community twice
    data = {"name": "Community 2"}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == 201

    response = client.post(ENDPOINT, json=data)
    assert response.status_code == 409


def test_patch_community_success(client):
    # assert that a community can be updated
    data = {"name": "Community 3"}
    response = client.post(ENDPOINT, json=data)
    assert response.status_code == 201
    id_ = response.json().get("id")

    data = {"is_active": False}
    response_patch = client.patch(f"{ENDPOINT}/{id_}", json=data)
    assert response_patch.status_code == 200

    # check new status
    response_get_json = client.get(f"{ENDPOINT}/{id_}").json()
    assert not response_get_json.get("is_active")
    assert response_get_json.get("last_updated_at") != response_get_json.get("created_at")


def test_patch_community_not_found(client):
    # test that we can't update a non-existing community
    non_existing_id = 100
    data = {"is": "Community 3"}
    response = client.patch(f"{ENDPOINT}/{non_existing_id}", json=data)
    assert response.status_code == 404
