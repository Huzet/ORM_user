"""empty message

Revision ID: 565e0f911f43
Revises: 01ac6a56b1c4
Create Date: 2020-02-23 12:33:12.635678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '565e0f911f43'
down_revision = '01ac6a56b1c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'age')
    # ### end Alembic commands ###
