"""empty message

Revision ID: 4b1009a75451
Revises: 5e1ab3f75d76
Create Date: 2020-12-27 15:36:12.181206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b1009a75451'
down_revision = '5e1ab3f75d76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_champion_spell_spell_code', table_name='champion_spell')
    op.drop_index('ix_champion_spell_spell_name', table_name='champion_spell')
    op.drop_table('champion_spell')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('champion_spell',
    sa.Column('champion_spell_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('champion_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('spell_code', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('spell_name', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['champion_id'], ['champion_list.champion_id'], name='champion_spell_champion_id_fkey'),
    sa.PrimaryKeyConstraint('champion_spell_id', name='champion_spell_pkey')
    )
    op.create_index('ix_champion_spell_spell_name', 'champion_spell', ['spell_name'], unique=False)
    op.create_index('ix_champion_spell_spell_code', 'champion_spell', ['spell_code'], unique=False)
    # ### end Alembic commands ###
