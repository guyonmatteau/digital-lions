"""Remove workshop cols

Revision ID: c999b3897e64
Revises: 553181df401b
Create Date: 2024-07-08 21:52:49.146185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'c999b3897e64'
down_revision: Union[str, None] = '553181df401b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workshops', 'cancellation_reason')
    op.drop_column('workshops', 'cancelled')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('workshops', sa.Column('cancelled', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('workshops', sa.Column('cancellation_reason', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
