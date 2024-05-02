from datetime import datetime
from typing import List, Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel

from models.community import Community


class Workshop(SQLModel, table=True):
    """Data model for workshops. A workshop is a session that took place
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""

    id: int = Field(default=None, primary_key=True)
    date: str  # format YYYY-MM-DD
    cycle: int = None
    cancelled: bool
    cancellation_reason: str = None

    community_id: int = Field(foreign_key="community.id")
    # community: Community | None = Relationship(back_populates="workshops")
