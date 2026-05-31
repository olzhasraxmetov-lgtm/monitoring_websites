"""add PagesORM

Revision ID: a793fac670f8
Revises: 
Create Date: 2026-05-31 13:08:24.801935

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a793fac670f8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('pages')
