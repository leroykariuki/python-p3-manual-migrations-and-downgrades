"""Renaming students to scholars

Revision ID: 0596b3ef011b
Revises: 791279dd0760
Create Date: 2023-12-13 02:41:45.581663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0596b3ef011b'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
