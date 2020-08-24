"""empty message

Revision ID: 983fb5d75ac2
Revises: b31a8d259652
Create Date: 2020-08-24 12:37:37.017734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '983fb5d75ac2'
down_revision = 'b31a8d259652'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('password_hash', sa.String(length=180), nullable=True),
    sa.Column('avatar', sa.String(length=80), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_list')
    # ### end Alembic commands ###
