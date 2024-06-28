"""Utility script to populate db with records."""

import requests

URL = "http://localhost:8000/api/v1"

communities = [{"name": "Community 1"}, {"name": "Community 2"}]
children = [
    {"first_name": "Child 1", "last_name": "Child 1", "community_id": 1},
    {"first_name": "Child 2", "last_name": "Child 2", "community_id": 2},
]

if __name__ == "__main__":
    for community in communities:
        response = requests.post(f"{URL}/communities", json=community)
        print(response.json())
    for child in children:
        response = requests.post(f"{URL}/children", json=child)
        print(response.json())
