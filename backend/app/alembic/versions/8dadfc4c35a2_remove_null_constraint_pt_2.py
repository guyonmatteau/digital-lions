"""Remove null constraint pt 2

Revision ID: 8dadfc4c35a2
Revises: 8c161ff0d706
Create Date: 2024-09-16 15:36:06.762325

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "8dadfc4c35a2"
down_revision: str | None = "8c161ff0d706"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
