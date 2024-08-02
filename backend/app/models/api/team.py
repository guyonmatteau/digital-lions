import datetime

from models.base import CreateProperties, MetadataColumns
from pydantic import BaseModel, Field


class TeamPostIn(BaseModel, CreateProperties):
    """API request model for creating a team."""

    class TeamCreateChild(BaseModel, CreateProperties):
        """API sub request model to create a child within a team."""

        first_name: str
        last_name: str
        age: int | None = Field(
            default=None,
            description="Age in years at the time of registration",
        )
        dob: datetime.date | None = Field(
            default=None, description="Date of birth in the format YYYY-MM-DD"
        )
        gender: str | None = Field(default=None, description="Gender of child")

    name: str = Field(description="Name of the team")
    children: list[TeamCreateChild] | None = Field(
        description="Optional list of children to add directly to the team.", default=[]
    )
    community_id: int = Field(description="ID of community the team belongs to")


class TeamGetOut(BaseModel):
    """API response model for getting a team."""

    class CommunityOut(BaseModel):
        """API response model community as part of team."""

        id: int
        name: str

    community: CommunityOut
    is_active: bool
    id: int
    name: str


class TeamGetByIdOut(BaseModel, MetadataColumns):
    """API response model for getting a team by ID."""

    class CommunityOut(BaseModel):
        """API response model community as part of team."""

        id: int = Field(description="ID of the community", example=1)
        name: str = Field(description="Name of the community", example="Khayelitsha")

    class ProgressOut(BaseModel):
        """API response model for status of team."""

        workshop: int = Field(description="Number of workshops completed", example=3)

    class ChildOut(BaseModel):
        """API response model for child as part of team."""

        id: int = Field(description="ID of the child", example=1)
        first_name: str = Field(description="First name of the child", example="Nelson")
        last_name: str = Field(description="Last name of the child", example="Mandela")

    id: int = Field(description="ID of the team", example=1)
    name: str = Field(description="Name of the team", example="The A-Team")
    community: CommunityOut
    children: list[ChildOut]
    progress: ProgressOut
    is_active: bool = Field(
        description="Whether the team is still active in the program", example=True
    )


class TeamGetWorkshopOut(BaseModel):
    """API response model for getting workshop for a team."""

    class ChildAttendance(BaseModel):
        """API response model for child attendance at a workshop."""

        attendance: str = Field(
            description="Attendance status of the child", examples=["present", "absent"]
        )
        child_id: int = Field(description="ID of the child", example=1)
        first_name: str = Field(description="First name of the child", example="Nelson")
        last_name: str = Field(description="Last name of the child", example="Mandela")

    date: str = Field(description="Date of the workshop", example="2021-01-01")
    workshop_number: int = Field(
        description="Number of the workshop in the program", example=1
    )
    workshop_id: int = Field(description="Unique workshop ID reference", example=1000)
    attendance: list[ChildAttendance]
