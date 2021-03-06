"""champion_stat

Revision ID: c0203a53f265
Revises: f91fcfb76659
Create Date: 2020-08-31 17:40:29.519173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0203a53f265'
down_revision = 'f91fcfb76659'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('champion_stat',
    sa.Column('champion_stat_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('champion_id', sa.Integer(), nullable=True),
    sa.Column('stat_code', sa.Integer(), nullable=False),
    sa.Column('stat_value', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['champion_id'], ['champion_list.champion_id'], ),
    sa.PrimaryKeyConstraint('champion_stat_id')
    )
    op.create_index(op.f('ix_champion_stat_stat_code'), 'champion_stat', ['stat_code'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_champion_stat_stat_code'), table_name='champion_stat')
    op.drop_table('champion_stat')
    # ### end Alembic commands ###
