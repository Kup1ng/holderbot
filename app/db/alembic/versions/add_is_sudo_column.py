"""add is_sudo column to servers table

Revision ID: add_is_sudo_column
Revises: 5c72d5b1f3aa
Create Date: 2023-10-31 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add_is_sudo_column'
down_revision = '5c72d5b1f3aa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('servers', sa.Column('is_sudo', sa.Boolean(), nullable=False, server_default='1'))


def downgrade() -> None:
    op.drop_column('servers', 'is_sudo')