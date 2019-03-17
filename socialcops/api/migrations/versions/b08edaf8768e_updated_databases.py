"""Updated Databases

Revision ID: b08edaf8768e
Revises: 
Create Date: 2019-03-14 15:50:06.896484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b08edaf8768e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('operation', sa.String(length=30), nullable=True),
    sa.Column('state', sa.String(length=30), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_operation'), 'tasks', ['operation'], unique=False)
    op.create_index(op.f('ix_tasks_state'), 'tasks', ['state'], unique=False)
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('path', sa.String(length=300), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_results_task_id'), 'results', ['task_id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=300), nullable=True),
    sa.Column('record_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_index(op.f('ix_users_task_id'), 'users', ['task_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_task_id'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_results_task_id'), table_name='results')
    op.drop_table('results')
    op.drop_index(op.f('ix_tasks_state'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_operation'), table_name='tasks')
    op.drop_table('tasks')
    # ### end Alembic commands ###
