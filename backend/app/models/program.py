from sqlmodel import Field, SQLModel


class Program(SQLModel, table=True):
    """Model for a coaching program. A coaching program is a set of workshops that
    a team follows. Each workshop is a session that took place with a team. This
    model is to define a blueprint for the workshops that a team will follow.
    The actual workshops (workshop_reports) are stored in the WorkshopReport model."""

    __table_args__ = {"extend_existing": True}
    id: int = Field(default=None, primary_key=True)
