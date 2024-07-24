import logging

import exceptions
from models.community import CommunityCreate
from services.base import BaseService

logger = logging.getLogger(__name__)


class CommunityService(BaseService):
    """Community service layer to do anything related to communities."""

    def create(self, obj: CommunityCreate):
        """Create a new community in the database.

        Args:
            obj (CommunityCreate): Community object to create.
        """
        if self._communities.where([("name", obj.name)]):
            raise exceptions.CommunityAlreadyExistsException(
                f"Community with name {obj.name} already exists."
            )
        community = self._communities.create(obj)
        self.commit()
        return community

    def get_all(self):
        """Get all objects from the table."""
        return self._communities.read_all()

    def get(self, object_id):
        """Get an object from the table by id."""
        return self._communities.read(object_id=object_id)

    def update(self, object_id: int, obj):
        return self._communities.update(object_id=object_id, obj=obj)

    def delete(self, object_id: int):
        return self._communities.delete(object_id=object_id)
