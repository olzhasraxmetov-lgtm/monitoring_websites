"""add unique param for url to PagesORM

Revision ID: 564e0f3933f4
Revises: a793fac670f8
Create Date: 2026-05-31 13:40:27.579730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '564e0f3933f4'
down_revision: Union[str, Sequence[str], None] = 'a793fac670f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(None, 'pages', ['url'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'pages', type_='unique')
