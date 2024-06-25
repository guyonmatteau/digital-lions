import logging

import bcrypt
from exceptions import ItemAlreadyExistsException, ItemNotFoundException, UserUnauthorizedException
from models.user import User, UserCreate, UserOut, UserUpdate
from repositories import UserRepository
from services.base import BaseService

logger = logging.getLogger()


class UserService(BaseService):
    """User service layer to do anything related to users."""

    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self._repository = user_repository

    def create_user(self, user: UserCreate):
        """Create a new user."""
        return self._user_repository.create(user)

    def create_workshop_report(self):
        """Create a report of the workshops the user has done."""
        pass

    def delete_user(self, user_id):
        return self._user_repository.delete_user(user_id)

    def add_user(self, user: UserCreate) -> UserOut:
        if self.db.query(User).filter(User.email_address == user.email_address).first():
            raise ItemAlreadyExistsException()

        # this should be part of the service
        hashed_password, salt = self._hash_password(user.password)
        extra_data = {"hashed_password": hashed_password, "salt": salt}
        db_user = User.model_validate(user, update=extra_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user: UserUpdate) -> UserOut:
        db_user = self.db.get(User, user_id)
        if not db_user:
            raise ItemNotFoundException()
        user_data = user.model_dump(exclude_unset=True)
        db_user.sqlmodel_update(user_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def login_user(self, user: User) -> UserOut:
        db_user = self.db.query(User).filter(User.email_address == user.email_address).first()
        if not db_user:
            raise ItemNotFoundException()
        hashed_password, _ = self._hash_password(user.password, db_user.salt)
        if db_user.hashed_password != hashed_password:
            raise UserUnauthorizedException()
        return db_user

    def _hash_password(password: str, salt: bytes = None) -> [bytes, bytes]:
        """Hash password."""
        salt = salt or bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes(password, "utf-8"), salt)
        return hashed_password, salt
