import logging

from repositories import ProgramRepository
from services.base import BaseService

logger = logging.getLogger(__name__)


class ProgramService(BaseService):
    """Program service layer to do anything related to programs."""

    def __init__(
        self,
        program_repository: ProgramRepository,
    ):
        self._repository = program_repository
