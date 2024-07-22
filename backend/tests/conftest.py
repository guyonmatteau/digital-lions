import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool


@pytest.fixture(name="session")
def session_fixture():
    """Create an in-memory SQLite database for testing."""
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)

    # this is the db fixture
    with Session(engine) as session:
        yield session


@pytest.fixture
def client(mocker, session):
    """Create a FastAPI test client."""
    # pytest runs from a different path then uvicorn so we need to mock the logger
    # before we import the app otherwise it will break on finding the logging conf
    # TODO setup logging in function + to app.settings
    mocker.patch("logging.config.fileConfig")

    from app.main import app

    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
