"""Add create_date to Projects and Tasks models.

Revision ID: 0cf52bce9ace
Revises: a6d966ee341c
Create Date: 2024-05-28 08:40:54.726751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf52bce9ace'
down_revision = 'a6d966ee341c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('create_date')

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('create_date')

    # ### end Alembic commands ###