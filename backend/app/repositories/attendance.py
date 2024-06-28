from models.attendance import Attendance
from repositories.base import BaseRepository


class AttendanceRepository(BaseRepository[Attendance]):
    """Repository to interact with Child table."""

    _model = Attendance
