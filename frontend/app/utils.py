import requests
import os
import json


class API:
    def __init__(self, url=None):
        self.url = url or os.environ.get("API_URL")
        if self.url is None:
            raise ValueError("API URL is not set")
        self.headers = {"Content-Type": "application/json"}

    def get_attendances(self):
        response = requests.get(f"{self.url}/attendances", headers=self.headers)
        return response

    def post_attendances(self, data):
        response = requests.post(
            f"{self.url}/attendances", data=json.dumps(data), headers=self.headers
        )
        return response

api = API(url="http://localhost:8000/api/v1")
communities = ["Community A", "Community B", "Community C"]
