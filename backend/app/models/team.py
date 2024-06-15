# from __future__ import annotations
#
# from sqlmodel import Field, Relationship, SQLModel
#
#
# class TeamBase(SQLModel):
#     """Base class for team model."""
#
#     name: str = Field(description="Name of the team", default=None, nullable=True)
#     community_id: int = Field(
#         description="ID of community the team is in", foreign_key="community.id"
#     )
#     program_id: int = Field(
#         description="ID of program the team is following",
#         foreign_key="program.id",
#         nullable=True,
#     )
#
#
# class Team(TeamBase, table=True):
#     """Data model for teams. A team is a group of children that
#     follow the Little Lions program: a set of workshops. The workshops
#     that the team follows are linked to the team as well."""
#
#     __table_args__ = {"extend_existing": True}
#
#     id: int = Field(default=None, primary_key=True)
#     program_tracker: int = Field(
#         description="The current workshop the team is at in the program", default=1
#     )
#     active: bool = Field(description="Whether the team is active or not", default=True)
#
#     # community: Community = Relationship(back_populates="teams")
#     # program: Program = Relationship(back_populates="teams")
#     # children: list[Child] | None = Relationship(back_populates="team")
#     # workshops: list[Workshop] | None = Relationship(back_populates="team")
