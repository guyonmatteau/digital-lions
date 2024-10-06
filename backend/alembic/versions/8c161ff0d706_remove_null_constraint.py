"""Remove null constraint

Revision ID: 8c161ff0d706
Revises: 88d441731023
Create Date: 2024-09-16 15:35:42.614642

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "8c161ff0d706"
down_revision: str | None = "88d441731023"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
