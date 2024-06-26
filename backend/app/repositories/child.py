from models.child import Child
from repositories.base import BaseRepository


class ChildRepository(BaseRepository[Child]):
    """Repository to interact with Child table."""

    _model = Child
