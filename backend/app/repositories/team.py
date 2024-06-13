import logging

from exceptions import ItemNotFoundException
from models.team import Team, TeamCreate
from repositories.base import BaseRepository

logger = logging.getLogger()


class TeamRepository(BaseRepository):
    """Repository to interact with Team table from database."""

    def create(self, team: TeamCreate) -> Team:
        new_team = Team.from_orm(team)
        self.db.add(new_team)
        self.db.refresh(new_team)
        self.db.commit()
        return new_team

    def read_all(self) -> list[Team]:
        return self.db.query(Team).all()

    def read(self, team_id: int) -> Team:
        team = self.db.get(Team, team_id)
        if not team:
            raise ItemNotFoundException()
        return team

    #
    # def update(self, child_id: int, child: ChildUpdate) -> ChildOut:
    #     db_child = self.db.get(Child, child_id)
    #     if not db_child:
    #         raise ItemNotFoundException()
    #
    #     child_data = child.model_dump(exclude_unset=True)
    #     db_child.sqlmodel_update(child_data)
    #     self.db.add(db_child)
    #     self.db.commit()
    #     self.db.refresh(db_child)
    #     return db_child
