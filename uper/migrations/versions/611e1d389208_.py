"""empty message

Revision ID: 611e1d389208
Revises: 
Create Date: 2019-03-29 16:14:33.878342

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '611e1d389208'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.Binary(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('shrub')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('name', mysql.TEXT(collation='utf8mb4_unicode_ci'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('shrub',
    sa.Column('id', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('name', mysql.TEXT(collation='utf8mb4_unicode_ci'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('roles')
    op.drop_table('users')
    # ### end Alembic commands ###
