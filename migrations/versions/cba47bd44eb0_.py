"""empty message

Revision ID: cba47bd44eb0
Revises: acd82c4197c3
Create Date: 2021-02-25 18:46:47.151307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cba47bd44eb0'
down_revision = 'acd82c4197c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('created', sa.String(length=250), nullable=True))
    op.add_column('people', sa.Column('edited', sa.String(length=250), nullable=True))
    op.add_column('people', sa.Column('gender', sa.String(length=250), nullable=True))
    op.add_column('people', sa.Column('homeworld', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('people', 'homeworld')
    op.drop_column('people', 'gender')
    op.drop_column('people', 'edited')
    op.drop_column('people', 'created')
    # ### end Alembic commands ###
