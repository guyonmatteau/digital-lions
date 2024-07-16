import logging

import exceptions
from models.child import ChildCreate
from repositories import AttendanceRepository, ChildRepository, TeamRepository
from services.base import BaseService

logger = logging.getLogger(__name__)


class ChildService(BaseService):
    """Team service layer to do anything related to teams."""

    def __init__(
        self,
        child_repository: ChildRepository,
        team_repository: TeamRepository,
        attendance_repository: AttendanceRepository,
    ):
        self._repository = child_repository
        self._team_repository = team_repository
        self._attendance_repository = attendance_repository

    def create(self, child: ChildCreate):
        """Create a new child."""
        try:
            self._team_repository.read(object_id=child.team_id)
        except exceptions.ItemNotFoundException:
            logger.error(f"Team with ID {child.team_id} not found")
            raise exceptions.TeamNotFoundException()
        return self._repository.create(child)

    def delete(self, object_id: int, cascade: bool = False):
        """Delete a child."""
        if self._attendance_repository.filter(attr="child_id", value=object_id):
            if not cascade:
                logger.error(f"Child with id {object_id} has attendance records.")
                raise exceptions.ChildHasAttendanceException()
            logger.info(f"Deleting attendance records for child with ID {object_id}")
            self._attendance_repository.delete_bulk(attr="child_id", value=object_id)
        logger.info(f"Deleting child with ID {object_id}")
        self._repository.delete(object_id=object_id)
