from typing import Annotated

from db.session import get_db
from fastapi import Depends
from sqlmodel import Session


class BaseRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self._db = db
