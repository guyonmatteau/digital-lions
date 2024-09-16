"""Remove null constraint

Revision ID: 88d441731023
Revises: b696385143e8
Create Date: 2024-09-16 15:33:00.752096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '88d441731023'
down_revision: Union[str, None] = 'b696385143e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
