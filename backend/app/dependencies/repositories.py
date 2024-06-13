from typing import Annotated

from db.session import get_db
from fastapi import Depends
from repositories.team import TeamRepository
from sqlmodel import Session


def get_team_repository(db: Annotated[Session, Depends(get_db)]):
    return TeamRepository(db=db)
