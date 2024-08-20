"""Utility script to populate db with records."""

import logging
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
URL = "https://backend-staging-ffae.up.railway.app/api/v1"

if __name__ == "__main__":
    """Wipe with records."""
    communities = requests.get(f"{URL}/communities").json()
    logger.info(f"Deleting {len(communities)} communities")
    for community in communities:
        logger.info(f"Deleting community {community['name']} with ID {community['id']}")
        response = requests.delete(
            f"{URL}/communities/{community['id']}", params={"cascade": True}
        )
        logger.info(response.json())
        response.raise_for_status()
