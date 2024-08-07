"""Remove col

Revision ID: 43d31a61becb
Revises: ef8cd6011991
Create Date: 2024-07-30 22:40:12.857287

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "43d31a61becb"
down_revision: Union[str, None] = "ef8cd6011991"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "children",
        "dob",
        existing_type=sa.VARCHAR(),
        type_=sa.Date(),
        existing_nullable=True,
    )
    op.drop_column("teams", "program_tracker")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "teams",
        sa.Column("program_tracker", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.alter_column(
        "children",
        "dob",
        existing_type=sa.Date(),
        type_=sa.VARCHAR(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###
