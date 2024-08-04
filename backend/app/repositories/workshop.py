from models.db.schema import Workshop
from repositories.base import BaseRepository
from sqlalchemy import func


class WorkshopRepository(BaseRepository[Workshop]):
    """Repository to interact with Workshop table."""

    _model = Workshop

    def get_last_workshop_per_team(self, team_ids: list[int]) -> dict:
        """For a list of team ID's, get the highest workshop number
        for each team.

        Args:
            team_ids (list[int]): List of team ID's to get aggregation for.

        Returns:
            dict: Dictionary with team ID as key and highest workshop number as value.
        """
        results = (
            self._session.query(
                self._model.team_id, func.max(self._model.workshop_number)
            )
            .filter(self._model.team_id.in_(team_ids))
            .group_by(self._model.team_id)
            .all()
        )

        result_dict = {team_id: workshop_number for team_id, workshop_number in results}
        return result_dict
