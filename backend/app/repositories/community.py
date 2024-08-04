from models.db.schema import Community
from repositories import BaseRepository


class CommunityRepository(BaseRepository[Community]):
    """Repository to interact with Community table."""

    _model = Community
