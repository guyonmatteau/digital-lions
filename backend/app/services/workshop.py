import logging

from repositories import WorkshopRepository
from services.base import BaseService

logger = logging.getLogger(__name__)


class WorkshopService(BaseService):
    """Workshop service layer to do anything related to workshops.
    In principle this should be always be done via a Teams service."""

    def __init__(
        self,
        workshop_repository: WorkshopRepository,
    ):
        self._repository = workshop_repository
