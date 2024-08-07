import datetime

from models.generic import CreateProperties, MetadataColumns, UpdateProperties
from pydantic import BaseModel, Field, field_validator, model_validator


class ChildValidators:
    """Validation methods for child model."""

    @field_validator("gender")
    def validate_gender(cls, v) -> str:
        """Validate that the gender is either male, female or null."""
        if v is not None and v not in ["male", "female"]:
            raise ValueError(
                f"Invalid gender, should be male, female or null. Got: {v}"
            )
        return v

    @field_validator("age")
    def validate_age(cls, v) -> int:
        """Validate that age is a positive integer."""
        if v is not None and v <= 0:
            raise ValueError(f"Age {v} is invalid")
        return v

    @model_validator(mode="after")
    def validate_age_or_dob(self):
        """Validate that either age or dob is provided, not both."""
        if self.age is not None and self.dob is not None:
            raise ValueError("Either age or dob should be provided, not both.")
        return self

    @field_validator("dob")
    def convert_dob_to_str(cls, v) -> str:
        """Convert dob to date format YYYY-MM-DD if it is provided."""
        if v is not None:
            v = v.strftime("%Y-%m-%d")
        return v


class ChildPostIn(BaseModel, CreateProperties, ChildValidators):
    """API payload model for creating a child. Either age
    or dob can be provided, not both."""

    first_name: str = Field(description="First name of child", example="Nelson")
    last_name: str = Field(description="Last name of child", example="Mandela")
    age: int | None = Field(
        description="Optional age in years at the time of registration",
        default=None,
        example=10,
    )
    dob: datetime.date | None = Field(
        description="Optional date of birth in the format YYYY-MM-DD",
        default=None,
        example="2001-01-01",
    )
    gender: str | None = Field(
        default=None,
        description="Optional gender of child. Either 'male', 'female' or null.",
        examples=["male", "female"],
    )
    team_id: int = Field(description="Team ID to which the child belongs", example=1)


class ChildPatchIn(BaseModel, UpdateProperties, ChildValidators):
    """API payload model for PATCH /children/:id for updating a child. 
    Either age or dob can be provided, not both."""

    first_name: str | None = Field(
        description="First name of child", example="Nelson", default=None
    )
    last_name: str | None = Field(
        description="Last name of child", example="Mandela", default=None
    )
    age: int | None = Field(
        description="Optional age in years at the time of registration",
        default=None,
        example=10,
    )
    dob: datetime.date | None = Field(
        description="Optional date of birth in the format YYYY-MM-DD",
        default=None,
        example="2001-01-01",
    )
    gender: str | None = Field(
        default=None,
        description="Optional gender of child. Either 'male', 'female' or null.",
        examples=["male", "female"],
    )



class ChildGetByIdOut(BaseModel, MetadataColumns):
    """Response model for GET /children/{id}."""

    id: int
    first_name: str
    last_name: str
    age: int | None = Field(
        default=None,
        description="Age in years at the time of registration",
    )
    dob: str | None = Field(
        default=None, description="Date of birth in the format YYYY-MM-DD"
    )
    gender: str | None = Field(
        default=None, description="Gender of child. Either male or female."
    )
    team_id: int

class ChildGetOut(BaseModel):
    """Response model for list response of GET /children."""

    first_name: str
    last_name: str
    id: int


