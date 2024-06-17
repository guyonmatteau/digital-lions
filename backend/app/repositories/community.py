from models.community import Community
from repositories import BaseRepository


class CommunityRepository(BaseRepository[Community]):
    """Repository to interact with Community table."""

    model = Community
