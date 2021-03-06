"""Initial Migration

Revision ID: 4c947572ef99
Revises: 5de80d2def63
Create Date: 2021-03-04 17:15:42.324649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c947572ef99'
down_revision = '5de80d2def63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('commenter', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'commenter')
    # ### end Alembic commands ###