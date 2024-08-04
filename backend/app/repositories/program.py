from models.db.schema import Program
from repositories.base import BaseRepository


class ProgramRepository(BaseRepository[Program]):
    """Repository to interact with Program table."""

    _model = Program
