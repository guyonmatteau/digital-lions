from models.community import Community
from repositories.base import BaseRepository


class CommunityRepository(BaseRepository[Community]):
    """Repository to interact with Community table."""

    model = Community
