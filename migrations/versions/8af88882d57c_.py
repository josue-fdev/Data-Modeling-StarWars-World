"""empty message

Revision ID: 8af88882d57c
Revises: f7dec95784d5
Create Date: 2021-02-25 15:43:23.973411

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8af88882d57c'
down_revision = 'f7dec95784d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favorites', 'people_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favorites', 'people_name',
               existing_type=mysql.VARCHAR(length=250),
               nullable=False)
    op.alter_column('favorites', 'planet_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favorites', 'planet_name',
               existing_type=mysql.VARCHAR(length=250),
               nullable=False)
    op.alter_column('favorites', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.create_unique_constraint(None, 'favorites', ['user_id'])
    op.create_unique_constraint(None, 'favorites', ['people_name'])
    op.create_unique_constraint(None, 'favorites', ['planet_name'])
    op.create_unique_constraint(None, 'favorites', ['people_id'])
    op.create_unique_constraint(None, 'favorites', ['planet_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'favorites', type_='unique')
    op.drop_constraint(None, 'favorites', type_='unique')
    op.drop_constraint(None, 'favorites', type_='unique')
    op.drop_constraint(None, 'favorites', type_='unique')
    op.drop_constraint(None, 'favorites', type_='unique')
    op.alter_column('favorites', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favorites', 'planet_name',
               existing_type=mysql.VARCHAR(length=250),
               nullable=True)
    op.alter_column('favorites', 'planet_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favorites', 'people_name',
               existing_type=mysql.VARCHAR(length=250),
               nullable=True)
    op.alter_column('favorites', 'people_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
