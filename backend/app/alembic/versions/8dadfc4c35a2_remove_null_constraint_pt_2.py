"""Remove null constraint pt 2

Revision ID: 8dadfc4c35a2
Revises: 8c161ff0d706
Create Date: 2024-09-16 15:36:06.762325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '8dadfc4c35a2'
down_revision: Union[str, None] = '8c161ff0d706'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
