import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(mocker):
    """Create a FastAPI test client."""
    # pytest runs from a different path then uvicorn so we need to mock the logger
    # before we import the app otherwise it will break on finding the logging conf
    # TODO setup logging in function + to app.settings
    mocker.patch("logging.config.fileConfig")

    from app.main import app

    client = TestClient(app)
    yield client
