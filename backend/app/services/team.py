import logging

import exceptions
from models.team import TeamCreate
from models.workshop import WorkshopCreate
from repositories import (
    AttendanceRepository,
    ChildRepository,
    CommunityRepository,
    TeamRepository,
    WorkshopRepository,
)
from services.base import BaseService

logger = logging.getLogger(__name__)


class TeamService(BaseService):
    """Team service layer to do anything related to teams."""

    def __init__(
        self,
        team_repository: TeamRepository,
        child_repository: ChildRepository,
        community_repository: CommunityRepository,
        workshop_repository: WorkshopRepository,
        attendance_repository: AttendanceRepository,
    ):
        self._repository = team_repository
        self._child_repository = child_repository
        self._community_repository = community_repository
        self._workshop_repository = workshop_repository
        self._attendance_repository = attendance_repository

    def create(self, team: TeamCreate):
        """Create a new team."""
        try:
            self._community_repository.read(object_id=team.community_id)
        except exceptions.ItemNotFoundException:
            logger.error(f"Community with ID {team.community_id} not found")
            raise exceptions.CommunityNotFoundException()

        # first create the team, then add children to it
        children = team.children
        delattr(team, "children")
        new_team = self._repository.create(team)
        logger.info(f"Team with id {new_team.id} created.")

        for child in children:
            child.team_id = new_team.id
            self._child_repository.create(child)
            logger.info("Child with id {} added to team {}.", child.id, new_team.id)
        return new_team

    def create_workshop(self, team_id: int, workshop: WorkshopCreate):
        """Create a workshop for a team."""
        try:
            self._repository.read(object_id=team_id)
        except exceptions.TeamNotFoundException:
            raise exceptions.TeamNotFoundException()

        attendance = workshop.attendance
        workshop.team_id = team_id
        delattr(workshop, "attendance")
        workshop_record = self._workshop_repository.create(workshop)

        for child_attendance in attendance:
            child_attendance.workshop_id = workshop_record.id
            self._attendance_repository.create(child_attendance)
        return workshop_record
