"""empty message

Revision ID: 094c79e968ca
Revises: 
Create Date: 2020-12-27 15:44:43.456275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '094c79e968ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('champion_list',
    sa.Column('champion_id', sa.Integer(), nullable=False),
    sa.Column('champion_name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('champion_id'),
    sa.UniqueConstraint('champion_name')
    )
    op.create_table('tag_list',
    sa.Column('tag_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tag_name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('tag_id'),
    sa.UniqueConstraint('tag_name')
    )
    op.create_table('user_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=180), nullable=False),
    sa.Column('avatar', sa.String(length=80), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('version_list',
    sa.Column('index', sa.Integer(), nullable=False),
    sa.Column('version_code', sa.String(length=20), nullable=False),
    sa.Column('upload_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('index'),
    sa.UniqueConstraint('version_code')
    )
    op.create_table('champion_spell',
    sa.Column('champion_spell_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('champion_id', sa.Integer(), nullable=False),
    sa.Column('spell_code', sa.Integer(), nullable=False),
    sa.Column('spell_name', sa.String(length=40), nullable=False),
    sa.ForeignKeyConstraint(['champion_id'], ['champion_list.champion_id'], ),
    sa.PrimaryKeyConstraint('champion_spell_id')
    )
    op.create_index(op.f('ix_champion_spell_spell_code'), 'champion_spell', ['spell_code'], unique=False)
    op.create_index(op.f('ix_champion_spell_spell_name'), 'champion_spell', ['spell_name'], unique=False)
    op.create_table('champion_stat',
    sa.Column('champion_stat_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('champion_id', sa.Integer(), nullable=False),
    sa.Column('stat_code', sa.Integer(), nullable=False),
    sa.Column('stat_value', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['champion_id'], ['champion_list.champion_id'], ),
    sa.PrimaryKeyConstraint('champion_stat_id')
    )
    op.create_index(op.f('ix_champion_stat_stat_code'), 'champion_stat', ['stat_code'], unique=False)
    op.create_table('champion_tag',
    sa.Column('champion_tag_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('champion_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['champion_id'], ['champion_list.champion_id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag_list.tag_id'], ),
    sa.PrimaryKeyConstraint('champion_tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('champion_tag')
    op.drop_index(op.f('ix_champion_stat_stat_code'), table_name='champion_stat')
    op.drop_table('champion_stat')
    op.drop_index(op.f('ix_champion_spell_spell_name'), table_name='champion_spell')
    op.drop_index(op.f('ix_champion_spell_spell_code'), table_name='champion_spell')
    op.drop_table('champion_spell')
    op.drop_table('version_list')
    op.drop_table('user_list')
    op.drop_table('tag_list')
    op.drop_table('champion_list')
    # ### end Alembic commands ###