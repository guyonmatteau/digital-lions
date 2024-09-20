"""Remove dob col

Revision ID: b696385143e8
Revises: 09d9cb9ceb8f
Create Date: 2024-08-15 21:47:05.248527

"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b696385143e8"
down_revision: str | None = "09d9cb9ceb8f"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("children", "dob")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("children", sa.Column("dob", sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
