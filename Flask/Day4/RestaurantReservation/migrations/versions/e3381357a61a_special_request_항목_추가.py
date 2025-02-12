"""special_request 항목 추가

Revision ID: e3381357a61a
Revises: 
Create Date: 2024-07-29 19:15:37.823551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3381357a61a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservations', schema=None) as batch_op:
        batch_op.drop_index('customer_phone')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservations', schema=None) as batch_op:
        batch_op.create_index('customer_phone', ['customer_phone'], unique=True)

    # ### end Alembic commands ###
