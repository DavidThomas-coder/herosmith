"""add_character_table

Revision ID: 742f11f9d051
Revises: d3c3a15aec74
Create Date: 2023-11-22 15:12:23.460892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '742f11f9d051'
down_revision = 'd3c3a15aec74'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'character',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('race', sa.String(length=80), nullable=False),
        sa.Column('char_class', sa.String(length=80), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('background', sa.String(length=300), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('character')

