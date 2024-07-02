import logging

from repositories import AttendanceRepository
from services.base import BaseService

logger = logging.getLogger(__name__)


class AttendanceService(BaseService):
    """Attendance service layer to do anything related to attendances.
    In principle this should be always be done via a Teams service."""

    def __init__(
        self,
        attendance_repository: AttendanceRepository,
    ):
        self._repository = attendance_repository
