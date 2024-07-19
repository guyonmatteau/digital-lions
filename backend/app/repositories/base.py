from enum import Enum
from typing import Generic, TypeVar

from dependencies.database import DatabaseDependency
from exceptions import ItemNotFoundException
from sqlalchemy import and_, delete
from sqlmodel import SQLModel

Model = TypeVar("Model", bound=SQLModel)
ModelCreate = TypeVar("ModelCreate", bound=SQLModel)
ModelUpdate = TypeVar("ModelUpdate", bound=SQLModel)
ModelOut = TypeVar("ModelOut", bound=SQLModel)


class Columns(str, Enum):
    """Enum for all columns in the database."""

    id = "id"
    name = "name"
    email_address = "email_address"
    password = "password"
    salt = "salt"
    hashed_password = "hashed_password"
    team_id = "team_id"
    workshop_number = "workshop_number"
    date = "date"
    attendance = "attendance"
    child_id = "child_id"
    workshop_id = "workshop_id"


class BaseRepository(Generic[Model]):
    """Generic repository template metaclass for all repositories that
    interact with a table in the database. Supports all classic CRUD
    operations as well as custom queries."""

    _model: type[Model]
    cols: Columns

    def __init__(self, db: DatabaseDependency):
        self._db: DatabaseDependency = db

    def create(self, obj: ModelCreate) -> ModelOut:
        """Create an object in the table."""
        new_obj = self._model.from_orm(obj)
        self._db.add(new_obj)
        self._db.commit()
        self._db.refresh(new_obj)
        return new_obj

    def delete(self, object_id: int) -> None:
        """Delete an object from the table."""
        obj = self._db.get(self._model, object_id)
        if not obj:
            raise ItemNotFoundException()
        self._db.delete(obj)
        self._db.commit()

    def delete_where(self, attr: str, value: str) -> None:
        """Delete all objects by an attribute matching a value."""
        statement = delete(self._model).where(getattr(self._model, attr) == value)
        self._db.exec(statement)
        self._db.commit()

    def read(self, object_id: int) -> ModelOut | None:
        """Read an object from the table."""
        obj = self._db.get(self._model, object_id)
        if not obj:
            raise ItemNotFoundException()
        return obj

    def read_all(self) -> list[ModelOut] | None:
        """Read all objects from the table."""
        objects = self._db.query(self._model).all()
        return objects

    def update(self, object_id: int, obj: ModelUpdate) -> ModelOut:
        """Update an object in the table."""
        db_object = self._db.get(self._model, object_id)
        if not db_object:
            raise ItemNotFoundException()

        obj_data = obj.model_dump(exclude_unset=True)
        db_object.sqlmodel_update(obj_data)
        self._db.add(db_object)
        self._db.commit()
        self._db.refresh(db_object)
        return db_object

    def where(self, filters: list[tuple[str, str]]) -> list[ModelOut] | None:
        """Filter table by one or more columns where all filters need to be met (AND).

        Args:
            filters (list[tuple[str, str]]): A list of tuples where each tuple contains
            the column name and the value to filter by. E.g. [("name", "John"), ("age", 25)].

        Returns:
            list[ModelOut]: A list of objects that meet all the filters.
        """
        expr = and_(*self._construct_filter(filters))
        return self._db.query(self._model).where(and_(expr)).all()

    def where_in(self, attr: str, values: list[str]) -> list[ModelOut] | None:
        """Filter table by an attribute where the attribute value is in a list of values.
        Args:
            attr (str): The attribute to filter by.
            values (list[str]): A list of values to filter by.
        Returns:
            list[ModelOut]: A list of objects that meet the filter.
        """
        return self._db.query(self._model).filter(getattr(self._model, attr).in_(values)).all()

    def query(self, query: str) -> list[ModelOut]:
        """Execute a custom query."""
        objects = self._db.exec(query)
        return objects

    def _construct_filter(self, filters: list[tuple[str, str]]) -> list:
        """Construct a filter from a list of tuples where each tuple
        contains the attribute and the value to filter by.

        Args:
            filters (list[tuple[str, str]]): A list of tuples where each tuple
                contains the attribute and the value to filter by. E.g.
                [("name", "John"), ("age", 25)].
        """
        filter_list = []
        for expr in filters:
            filter_list.append(getattr(self._model, expr[0]) == expr[1])
        return filter_list
