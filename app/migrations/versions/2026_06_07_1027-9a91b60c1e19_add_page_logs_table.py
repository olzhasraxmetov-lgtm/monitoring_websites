"""add_page_logs table

Revision ID: 9a91b60c1e19
Revises: 564e0f3933f4
Create Date: 2026-06-07 10:27:41.328825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '9a91b60c1e19'
down_revision: Union[str, Sequence[str], None] = '564e0f3933f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('page_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('page_id', sa.Integer(), nullable=False),
    sa.Column('status_code', sa.Integer(), nullable=True),
    sa.Column('response_time', sa.Float(), nullable=True),
    sa.Column('checked_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['page_id'], ['pages.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('page_logs')
