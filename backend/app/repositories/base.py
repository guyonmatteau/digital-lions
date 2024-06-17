from typing import Generic, TypeVar

from dependencies.database import DatabaseDependency
from exceptions import ItemNotFoundException
from models import child, community, team
from models.out import ChildOut, CommunityOut, TeamOut

Model = TypeVar("Model", community.Community, child.Child, team.Team)
ModelCreate = TypeVar("ModelCreate", community.CommunityCreate, child.ChildCreate, team.TeamCreate)
ModelUpdate = TypeVar("ModelUpdate", community.CommunityUpdate, child.ChildUpdate, team.TeamUpdate)
ModelOut = TypeVar("ModelOut", CommunityOut, ChildOut, TeamOut)


class BaseRepository(Generic[Model]):
    """Generic repository template metaclass for all repositories that
    interact with a table in the database. Supports all classic CRUD
    operations as well as custom queries."""

    _model: type[Model]

    def __init__(self, db: DatabaseDependency):
        self._db: DatabaseDependency = db

    def create(self, obj: ModelCreate) -> ModelOut:
        """Create an object in the table."""
        new_obj = self._model.from_orm(obj)
        self._db.add(new_obj)
        self._db.commit()
        self._db.refresh(new_obj)
        return new_obj

    def read(self, object_id: int) -> ModelOut:
        """Read an object from the table."""
        obj = self._db.get(self._model, object_id)
        if not obj:
            raise ItemNotFoundException()
        return obj

    def read_all(self) -> list[ModelOut]:
        """Read all objects from the table."""
        objects = self._db.query(self._model).all()
        return objects

    def update(self, object_id: int, obj: ModelUpdate) -> ModelOut:
        """Update an object in the table."""

        db_object = self._db.get(self._model, object_id)
        if not db_object:
            raise ItemNotFoundException()

        obj_data = obj_model_dump(exclude_unset=True)
        db_object.sqlmodel_update(obj_data)
        self._db.add(db_object)
        self._db.commit()
        self._db.refresh(db_object)
        return db_object

    def query(self, query: str) -> list[ModelOut]:
        """Execute a custom query."""
        objects = self._db.execute(query)
        return objects
