"""Initial Migration

Revision ID: c22c49faf1b5
Revises: 4c947572ef99
Create Date: 2021-03-06 20:14:51.189056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c22c49faf1b5'
down_revision = '4c947572ef99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###
