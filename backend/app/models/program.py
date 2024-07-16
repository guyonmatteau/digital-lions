from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel


class Program(SQLModel, table=True):
    """Data model for workshop programs. A program is a set of workshops that a team
    follows. It is used to track the progress of a team through the workshops. The table's
    ID column (PK) is an indicator (FK on Team's table) of where a team is in the program.

    Example:
        With program_id 1, workshop 0, the Team has not started the pgram yet.
        With program_id 1, workshop 1, the Team has completed workshop 1.
    """

    __tablename__ = "programs"

    id: int = Field(default=None, primary_key=True)
    program_id: int = Field()
    workshop: int = Field()
    workshop_name: str = Field(default=None)


class DefaultProgram(BaseModel):
    """Placeholder for Program model, to be implemented later."""

    program_id: int = 1
    program: list = [
        {"workshop_number": n, "date": None, "workshop_id": None, "attendance": []}
        for n in range(1, 13)
    ]
    workshops_done: list

    def __post_init__(self):
        pass
        # self.workshops = [Workshop(**workshop) for workshop in self.workshops]
