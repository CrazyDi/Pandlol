"""empty message

Revision ID: 9c63a78dafd4
Revises: 1f8252c54909
Create Date: 2020-08-25 17:15:22.259108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c63a78dafd4'
down_revision = '1f8252c54909'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('version_list',
    sa.Column('version_code', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('version_code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('version_list')
    # ### end Alembic commands ###
