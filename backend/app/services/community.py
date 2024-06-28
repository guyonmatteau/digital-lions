import logging

import exceptions
from models.community import CommunityCreate
from repositories import CommunityRepository
from services.base import BaseService

logger = logging.getLogger(__name__)


class CommunityService(BaseService):
    """Team service layer to do anything related to teams."""

    def __init__(
        self,
        community_repository: CommunityRepository,
    ):
        self._repository = community_repository

    def create(self, obj: CommunityCreate):
        """Create a new object on the repository."""
        if self._repository.filter(attr="name", value=obj.name):
            raise exceptions.CommunityAlreadyExistsException(
                f"Community with name {obj.name} already exists."
            )
        return self._repository.create(obj)
