import logging

import exceptions
from models.child import ChildCreate
from models.team import TeamCreate
from models.workshop import WorkshopCreate, WorkshopCreateInDB
from repositories import (
    AttendanceRepository,
    ChildRepository,
    CommunityRepository,
    TeamRepository,
    WorkshopRepository,
)
from repositories.base import Columns
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
        self.cols = Columns

    def create(self, team: TeamCreate):
        """Create a new team."""
        try:
            self._community_repository.read(object_id=team.community_id)
        except exceptions.ItemNotFoundException:
            msg = f"Community with ID {team.community_id} not found"
            logger.error(msg)
            raise exceptions.CommunityNotFoundException(msg)

        # first create the team, then add children to it
        children = team.children
        delattr(team, "children")
        new_team = self._repository.create(team)
        logger.info(f"Team with ID {new_team.id} created.")

        for child in children:
            child_in = ChildCreate(team_id=new_team.id, **child.dict())
            child_created = self._child_repository.create(child_in)
            logger.info("Child with ID %d added to team %d.", child_created.id, new_team.id)
        return new_team

    def create_workshop(self, team_id: int, workshop: WorkshopCreate):
        """Create a workshop for a team."""
        self._validate_team_exists(team_id)

        # validate that workshop does not exist yet
        if self._workshop_repository.where(
            [
                (self.cols.team_id, team_id),
                (self.cols.workshop_number, workshop.workshop_number),
            ]
        ):
            error_msg = f"Workshop {workshop.workshop_number} for team {team_id} already exists."
            logger.error(error_msg)
            raise exceptions.WorkshopExistsException(error_msg)

        attendance = workshop.attendance
        workshop_in = WorkshopCreateInDB(
            team_id=team_id,
            date=workshop.date,
            workshop_number=workshop.workshop_number,
        )

        workshop_record = self._workshop_repository.create(workshop_in)

        for child_attendance in attendance:
            if not self._child_repository.where(
                [
                    (self.cols.id, child_attendance.child_id),
                    (self.cols.team_id, team_id),
                ]
            ):
                error_msg = (
                    f"Child with ID {child_attendance.child_id} is not part of team {team_id}"
                )
                logger.error(error_msg)
                raise exceptions.ChildNotInTeam(error_msg)

            child_attendance.workshop_id = workshop_record.id
            self._attendance_repository.create(child_attendance)

        return workshop_record

    def delete(self, object_id: int, cascade: bool = False):
        """Delete a team."""

        if self._child_repository.where([(self.cols.team_id, object_id)]):
            if not cascade:
                error_msg = f"Team with ID {object_id} not empty: has children."
                logger.error(error_msg)
                raise exceptions.TeamHasChildrenException(error_msg)

            logger.info(f"Deleting children from team with ID {object_id}")
            self._child_repository.delete_bulk(attr="team_id", value=object_id)

        logger.info(f"Deleting team with ID {object_id}")
        self._repository.delete(object_id=object_id)

    def get_workshops(self, team_id: int) -> list | None:
        """Get all workshops for a team."""
        self._validate_team_exists(team_id)

        # TODO return workshop in context of program
        return self._workshop_repository.where([(self.cols.team_id, team_id)])

    @classmethod
    def from_factory(cls):
        """Factory function to create a standalone TeamService instance."""
        pass

    def _validate_team_exists(self, team_id: int) -> None:
        """Check if a team exists."""
        try:
            self._repository.read(object_id=team_id)
        except exceptions.ItemNotFoundException:
            msg = f"Team with ID {team_id} not found"
            logger.error(msg)
            raise exceptions.TeamNotFoundException(msg)
