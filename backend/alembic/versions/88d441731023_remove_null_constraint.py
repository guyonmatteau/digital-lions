"""Remove null constraint

Revision ID: 88d441731023
Revises: b696385143e8
Create Date: 2024-09-16 15:33:00.752096

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "88d441731023"
down_revision: str | None = "b696385143e8"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
