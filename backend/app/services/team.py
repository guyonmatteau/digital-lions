import logging

import exceptions
from models.child import ChildCreate
from models.team import TeamCreate
from models.workshop import WorkshopCreate, WorkshopCreateAttendanceInDB, WorkshopCreateInDB
from services.base import AbstractService, BaseService

logger = logging.getLogger(__name__)


class TeamService(AbstractService, BaseService):
    """Team service layer to do anything related to teams."""

    def create(self, team: TeamCreate):
        """Create a new team."""
        try:
            self._communities.read(object_id=team.community_id)
        except exceptions.ItemNotFoundException:
            msg = f"Community with ID {team.community_id} not found"
            logger.error(msg)
            raise exceptions.CommunityNotFoundException(msg)

        # first create the team, then add children to it
        children = team.children
        delattr(team, "children")
        new_team = self._teams.create(team)
        logger.info(f"Team with ID {new_team.id} created.")

        for child in children:
            child_in = ChildCreate(team_id=new_team.id, **child.dict())
            child_created = self._children.create(child_in)
            logger.info("Child with ID %d added to team %d.", child_created.id, new_team.id)

        self.commit()
        return new_team

    def create_workshop(self, team_id: int, workshop: WorkshopCreate):
        """Create a workshop for a team."""
        self._validate_team_exists(team_id)

        # validate that workshop does not exist yet for the team
        if self._workshops.where(
            [
                (self.cols.team_id, team_id),
                (self.cols.workshop_number, workshop.workshop_number),
            ]
        ):
            error_msg = f"Workshop {workshop.workshop_number} for team {team_id} already exists."
            logger.error(error_msg)
            raise exceptions.WorkshopExistsException(error_msg)

        # validate that the workshop number is the next valid workshop for the team
        workshops = self._workshops.where([(self.cols.team_id, team_id)])
        valid_workshop_number = (
            max(w.workshop_number for w in workshops) + 1 if len(workshops) > 0 else 1
        )
        if workshop.workshop_number != valid_workshop_number:
            error_msg = (
                f"Workshop number {workshop.workshop_number} is not the next correct "
                + f"workshop for team {team_id}. Should be {valid_workshop_number}"
            )
            logger.error(error_msg)
            raise exceptions.WorkshopNumberInvalidException(error_msg)

        # validate that all children in the payload are part of the team
        payload_child_ids = set([child.child_id for child in workshop.attendance])
        team_child_ids = set(
            [child.id for child in self._children.where([(self.cols.team_id, team_id)])]
        )

        payload_child_ids_not_in_team = [i for i in payload_child_ids if i not in team_child_ids]
        if payload_child_ids_not_in_team:
            error_msg = (
                "Payload attendance field contains children ID's that "
                + f"are not in team {team_id}: {payload_child_ids_not_in_team}"
            )
            logger.error(error_msg)
            raise exceptions.ChildNotInTeam(error_msg)

        # validate that all children from the team are in the payload
        team_child_ids_not_in_payload = [i for i in team_child_ids if i not in payload_child_ids]
        if team_child_ids_not_in_payload:
            error_msg = (
                "Attendance payload incomplete. Missing child ID's from "
                + f"team {team_id}: {team_child_ids_not_in_payload}"
            )
            logger.error(error_msg)
            raise exceptions.WorkshopIncompleteAttendance(error_msg)

        # create workshop
        attendance = workshop.attendance
        workshop_in = WorkshopCreateInDB(
            team_id=team_id,
            date=workshop.date,
            workshop_number=workshop.workshop_number,
        )
        workshop_record = self._workshops.create(workshop_in)

        # create attendance records for all children in team
        for child_attendance in attendance:
            attendance_in = WorkshopCreateAttendanceInDB(
                workshop_id=workshop_record.id,
                child_id=child_attendance.child_id,
                attendance=child_attendance.attendance,
            )
            self._attendances.create(attendance_in)

        self.commit()
        return workshop_record

    def get_all(self, filters=list[tuple]):
        """Get all objects from the table."""
        if filters:
            return self._teams.where(filters=filters)
        return self._teams.read_all()

    def get(self, object_id):
        """Get a team from the table by id."""
        try:
            return self._teams.read(object_id=object_id)
        except exceptions.ItemNotFoundException:
            error_msg = f"Team with ID {object_id} not found"
            logger.error(error_msg)
            raise exceptions.TeamNotFoundException(error_msg)

    def update(self, object_id: int, obj):
        return self._teams.update(object_id=object_id, obj=obj)

    def delete(self, object_id: int, cascade: bool = False):
        """Delete a team."""

        if self._children.where([(self.cols.team_id, object_id)]):
            if not cascade:
                error_msg = f"Team with ID {object_id} not empty: has children."
                logger.error(error_msg)
                raise exceptions.TeamHasChildrenException(error_msg)

            logger.info(f"Deleting children from team with ID {object_id}")
            self._children.delete_bulk(attr="team_id", value=object_id)

        logger.info(f"Deleting team with ID {object_id}")
        self._teams.delete(object_id=object_id)

    def get_workshops(self, team_id: int) -> list | None:
        """Get all workshops for a team."""
        self._validate_team_exists(team_id)

        # TODO return workshop in context of program
        return self._workshops.where([(self.cols.team_id, team_id)])

    def _validate_team_exists(self, team_id: int) -> None:
        """Check if a team exists."""
        try:
            self._teams.read(object_id=team_id)
        except exceptions.ItemNotFoundException:
            error_msg = f"Team with ID {team_id} not found"
            logger.error(error_msg)
            raise exceptions.TeamNotFoundException(error_msg)

    @classmethod
    def factory(cls):
        """Factory method to get service when not in dependency context."""
        raise NotImplementedError()
