import logging

import bcrypt
import exceptions
from database.schema import User
from models.api import Message, RecordCreated
from models.api.user import (UserGetByIdOut, UserPostIn, UserSessionOut,
                             UserUpdate)
from services.base import AbstractService, BaseService

logger = logging.getLogger()


class UserService(BaseService, AbstractService):
    """User service layer to do anything related to users."""

    PASSWORD_ENCODING: str = "utf-8"

    def create(self, user: UserPostIn) -> RecordCreated:
        """Create a new user."""

        # validate email address does not exist already
        if self.users.where([("email_address", user.email_address)]):
            raise exceptions.UserEmailAlreadyExistsException(
                f"A user with email {user.email_address} already exists."
            )

        # get hashed password and salt
        hashed_pwd, salt = self._hash_password(user.password)

        user = User(hashed_password=hashed_pwd, salt=salt, **user.dict())
        new_user = self.users.create(user)
        self.commit()
        return new_user

    def get_all(self) -> list[User] | None:
        """Get all users from the table."""
        return self.users.read_all()

    def get(self, user_id) -> User:
        """Get a User from the table by id."""
        try:
            return self.users.read(object_id=user_id)
        except exceptions.ItemNotFoundException:
            msg = f"User with ID {user_id} not found."
            logger.error(msg)
            raise exceptions.UserNotFoundException(msg)

    def update(self, user_id: int, user: UserUpdate) -> UserGetByIdOut:
        """Update a user."""

        self._validate_user_exists(user_id)

        # TODO do some validations
        user = self.users.update(object_id=user_id, obj=user)
        self.commit()
        return user

    def delete(self, user_id: int):
        """Delete a user by id."""
        try:
            self._user_repository.delete_user(user_id)
            self.commit()
            return Message(detail=f"User with ID {user_id} deleted.")
        except exceptions.ItemNotFoundException:
            raise exceptions.UserNotFoundException(f"User with ID {user_id} not found.")

    def login(self, user: User) -> UserSessionOut:
        """Get session token for user."""

        try:
            user = self._validate_user_exists(user)
        except exceptions.ItemNotFoundException:
            raise exceptions.UserNotFoundException(
                f"User with email {user.email_address} not found."
            )

        #
        return jwt

    def forgot(self, email_address: str) -> Message:
        """Send forgot password email to user."""
        if not self.users.where([("email_address", email_address)]):
            raise exceptions.UserNotFoundException(
                f"User with email {email_address} not found."
            )
        pass

    def _hash_password(self, password: str, salt: bytes = None) -> [bytes, bytes]:
        """Hash password. If salt is not provided (i.e. during user creation),
        then create a new salt and return it with the hashed password. If salt is
        provided (i.e. during user login), then use the provided salt to hash the password.

        Args:
            password (str): plain password to be hashed.
            salt (str | None): salt to use in hashing.
        """
        salt = salt or bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes(password, self.PASSWORD_ENCODING), salt)
        return hashed_password, salt

    def _validate_user_exists(self, user_id: int) -> User:
        """Check if user exists in the database."""
        user = self.users.read(object_id=user_id)
        if not user:
            raise exceptions.ItemNotFoundException()
        return user

    def _create_jwt(self, user: User) -> UserSessionOut:
        """Create a JWT token for the user."""
        pass

    def _get_user_by_email(
        self, email_address: str
    ) -> User | exceptions.UserNotFoundException:
        """Get a user by email address."""
        try:
            return self.users.where([("email_address", email_address)]).first()
        except exceptions.ItemNotFoundException:
            raise exceptions.UserNotFoundException(
                f"User with email {email_address} not found."
            )
