"""empty message

Revision ID: 94402883f075
Revises: 
Create Date: 2020-05-14 17:44:37.910439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94402883f075'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('project_name', sa.String(length=50), nullable=False),
    sa.Column('project_region', sa.String(length=200), nullable=False),
    sa.Column('project_version', sa.String(length=50), nullable=False),
    sa.Column('project_create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('user',
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('module',
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('module_name', sa.String(length=50), nullable=False),
    sa.Column('module_region', sa.String(length=200), nullable=False),
    sa.Column('module_create_time', sa.DateTime(), nullable=True),
    sa.Column('project_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('case',
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('case_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('case_name', sa.String(length=100), nullable=False),
    sa.Column('case_url', sa.String(length=100), nullable=False),
    sa.Column('case_type', sa.String(length=100), nullable=False),
    sa.Column('case_data', sa.Text(), nullable=False),
    sa.Column('case_create_time', sa.DateTime(), nullable=True),
    sa.Column('project_id', sa.String(length=50), nullable=True),
    sa.Column('module_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['module_id'], ['module.uuid'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('case')
    op.drop_table('module')
    op.drop_table('user')
    op.drop_table('project')
    # ### end Alembic commands ###
