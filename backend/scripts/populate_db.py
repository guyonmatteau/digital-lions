"""Utility script to populate db with records."""

import logging
import random
import sys

import requests
from faker import Faker

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

LOCALE = "zu_ZA"
URL = "http://localhost:8000/api/v1"
URL = "https://backend-production-7bbc.up.railway.app/api/v1"
COMMUNITY_COUNT = 5
TEAM_COUNT = 10
CHILD_COUNT = 20

fake = Faker(LOCALE)
Faker.seed(9)

if __name__ == "__main__":
    """Populate db with records, to be converted to integration test."""

    logger.info(f"Adding {COMMUNITY_COUNT} communities to the db")
    for _ in range(COMMUNITY_COUNT):
        community = {"name": fake.first_name()}
        logger.info(f"Creating community {community['name']}")
        response = requests.post(f"{URL}/communities", json=community)
        response.raise_for_status()
        logger.info(f"Community {community['name']} created with id {response.json()['id']}")

    logger.info(f"Adding {TEAM_COUNT} teams to the db")
    for _ in range(TEAM_COUNT):
        team = {
            "name": f"Team {fake.first_name()}",
            "community_id": random.randint(1, COMMUNITY_COUNT),
            "children": [
                {
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "gender": random.choice(["male", "female", None]),
                    **random.choice(
                        [
                            {"age": random.choice([random.randint(5, 18), None])},
                            {
                                "dob": f"{random.randint(2000, 2020)}-{random.randint(1, 12)}-{random.randint(1, 30)}"
                            },
                        ],
                    ),
                }
                for _ in range(CHILD_COUNT)
            ],
        }
        logger.info(f"Creating team {team}")
        try:
            response = requests.post(f"{URL}/teams", json=team)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f"Error creating team: {response.text}")
