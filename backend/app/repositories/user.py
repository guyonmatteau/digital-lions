import logging
from typing import Annotated

import bcrypt
from exceptions import (
    ItemAlreadyExistsException,
    ItemNotFoundException,
    UserUnauthorizedException,
)
from fastapi import Depends
from models.user import User, UserCreate, UserLogin, UserOut, UserUpdate
from repositories.base import BaseRepository

logger = logging.getLogger()


# hashing should actually be part of the service
def _hash_password(password: str, salt: bytes = None) -> [bytes, bytes]:
    """Hash password."""
    salt = salt or bcrypt.gensalt()
    logger.info(f"SALT: {salt}")
    hashed_password = bcrypt.hashpw(bytes(password, "utf-8"), salt)
    return hashed_password, salt


class UserRepository(BaseRepository):
    """Repository to interact with User table from Postgres _db."""

    # note this class currently does also some business logic, to be moved to service layer later

    def get_users(self) -> list[User]:
        return self._db.query(User).all()

    def get_user(self, user_id: int) -> User:
        user = self._db.get(User, user_id)
        if not user:
            raise ItemNotFoundException()
        return user

    def add_user(self, user: UserCreate) -> UserOut:
        if (
            self._db.query(User)
            .filter(User.email_address == user.email_address)
            .first()
        ):
            raise ItemAlreadyExistsException()

        # this should be part of the service
        hashed_password, salt = _hash_password(user.password)
        extra_data = {"hashed_password": hashed_password, "salt": salt}
        _db_user = User.model_validate(user, update=extra_data)
        self._db.add(_db_user)
        self._db.commit()
        self._db.refresh(_db_user)
        return _db_user

    def update_user(self, user_id: int, user: UserUpdate) -> UserOut:
        _db_user = self._db.get(User, user_id)
        if not _db_user:
            raise ItemNotFoundException()
        user_data = user.model_dump(exclude_unset=True)
        _db_user.sqlmodel_update(user_data)
        self._db.add(_db_user)
        self._db.commit()
        self._db.refresh(_db_user)
        return _db_user

    def login_user(self, user: User) -> UserOut:
        _db_user = (
            self._db.query(User)
            .filter(User.email_address == user.email_address)
            .first()
        )
        if not _db_user:
            raise ItemNotFoundException()
        hashed_password, _ = _hash_password(user.password, _db_user.salt)
        if _db_user.hashed_password != hashed_password:
            raise UserUnauthorizedException()
        return _db_user
