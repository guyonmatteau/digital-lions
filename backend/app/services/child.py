import logging

import exceptions
from dependencies.repositories import UnitOfWork
from models.child import ChildCreate

logger = logging.getLogger(__name__)


class ChildService(UnitOfWork):
    """Service layer to interact with children."""

    def create(self, child: ChildCreate):
        """Create a new child."""
        self._validate_team_exists(child.team_id)

        child = self._children.create(child)
        self.commit()
        return child

    def delete(self, object_id: int, cascade: bool = False):
        """Delete a child."""

        # check if child has attendance records
        if self._attendances.where([("child_id", object_id)]):
            # if cascade is False, raise an exception
            if not cascade:
                error_msg = f"Child with ID {object_id} has attendance records."
                logger.error(error_msg)
                raise exceptions.ChildHasAttendanceException(error_msg)

            # if cascade is True, delete all attendance records for the child
            logger.info(f"Deleting attendance records for child with ID {object_id}")
            self._attendances.delete_bulk(attr="child_id", value=object_id)

        # if child has no attendance records, delete the child
        logger.info(f"Deleting child with ID {object_id}")
        self._children.delete(object_id=object_id)
        self.commit()

    def get_all(self):
        """Get all objects from the table."""
        return self._children.read_all()

    def get(self, object_id):
        """Get a child by ID.

        Args:
            object_id (int): ID of the child to get.
        """
        try:
            return self._children.read(object_id=object_id)
        except exceptions.ItemNotFoundException:
            raise exceptions.ChildNotFoundException(f"Child with ID {object_id} not found")

    def update(self, object_id: int, obj):
        """Update a child.

        Args:
            object_id (int): ID of the child to update.
            obj (ChildUpdate): Child object with updated fields.
        """
        child = self._children.update(object_id=object_id, obj=obj)
        self.commit()
        return child

    def _validate_team_exists(self, team_id: int):
        """Validate that a team exists."""
        try:
            self._teams.read(object_id=team_id)
        except exceptions.ItemNotFoundException:
            error_msg = f"Team with ID {team_id} not found"
            logger.error(error_msg)
            raise exceptions.TeamNotFoundException(error_msg)
