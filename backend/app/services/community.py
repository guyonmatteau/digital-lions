import logging

import exceptions
from dependencies.database import SessionDependency
from dependencies.repositories import Repositories
from models.community import CommunityCreate
from repositories import CommunityRepository
from services.base import BaseService

logger = logging.getLogger(__name__)


class CommunityService(BaseService):
    """Community service layer to do anything related to communities."""

    def __init__(self, session: SessionDependency):
        self._session = session
        self._repositories = Repositories(session=self._session)
        self._repository: CommunityRepository = self._repositories.community

    def create(self, obj: CommunityCreate):
        """Create a new object on the repository."""
        if self._repository.where([("name", obj.name)]):
            raise exceptions.CommunityAlreadyExistsException(
                f"Community with name {obj.name} already exists."
            )
        community = self._repository.create(obj)
        self._repositories.commit()
        return community
