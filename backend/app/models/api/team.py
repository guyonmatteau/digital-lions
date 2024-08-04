import datetime

from models.generic import CreateProperties, MetadataColumns
from pydantic import BaseModel, Field, field_validator


class TeamPostIn(BaseModel, CreateProperties):
    """API payload model for POST /teams."""

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

        @field_validator("dob")
        def convert_dob_to_str(cls, v) -> str:
            """Convert dob to date format YYYY-MM-DD if it is provided."""
            if v is not None:
                v = v.strftime("%Y-%m-%d")
            return v

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
    """API response model for GET /teams/:id."""

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
    """API response model for GET /teams/:id/workshops."""

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


class TeamPostWorkshopIn(BaseModel):
    """API payload model for POST /teams/:id/workshops."""

    class Attendance(BaseModel):
        """Model for adding attendance to a workshop, part
        of the WorkshopPostIn payload."""

        attendance: str = Field(
            description="Attendance status of the child to the workshop. "
            "Must be 'present', 'absent', or 'cancelled'."
        )
        child_id: int = Field(description="ID of the child")

        @field_validator("attendance")
        def validate_attendance(cls, v):
            if v not in ["present", "absent", "cancelled"]:
                raise ValueError(
                    "Attendance must be either 'present' or 'absent' or 'cancelled'"
                )
            return v

    date: datetime.date = Field(
        description="The date of the workshop in the format YYYY-MM-DD"
    )
    workshop_number: int = Field(
        description="The number of the workshop in the program, which must be between 1 and 12."
    )
    attendance: list[Attendance] | None = Field(
        description="List of attendance records of all children in the team."
    )

    @field_validator("workshop_number")
    def workshop_number_in_default_range(cls, v):
        """Validate that the workshop number is between 1 and 12."""
        if v not in range(1, 13):
            raise ValueError("Workshop number must be between 1 and 12.")
        return v

    @field_validator("date")
    def convert_dob_to_str(cls, v) -> str:
        """Convert date to date format YYYY-MM-DD if it is provided."""
        if v is not None:
            v = v.strftime("%Y-%m-%d")
        return v
