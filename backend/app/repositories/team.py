from models.team import Team
from repositories import BaseRepository


class TeamRepository(BaseRepository[Team]):
    """Repository to interact with Community table."""

    _model = Team
