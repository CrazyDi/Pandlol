"""empty message

Revision ID: 2c8485bee579
Revises: 983fb5d75ac2
Create Date: 2020-08-25 16:42:16.841506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c8485bee579'
down_revision = '983fb5d75ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=180), nullable=False),
    sa.Column('avatar', sa.String(length=80), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_index('ix_version_list_index', table_name='version_list')
    op.drop_table('version_list')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_list')
    # ### end Alembic commands ###