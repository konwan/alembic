"""delete a column from person

Revision ID: 698a3d124685
Revises: 3715f217a003
Create Date: 2016-11-11 17:06:20.881246

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '698a3d124685'
down_revision = '3715f217a003'
branch_labels = None
depends_on = None


def upgrade():
    # sqlite not support  op.drop_column('person', 'idcard')
    with op.batch_alter_table('person') as batch_op:
        batch_op.drop_column('idcard')


def downgrade():
    op.add_column('person', sa.Column('idcard', sa.String(length=20), nullable=True))

