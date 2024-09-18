"""cambio password a pasword_hash

Revision ID: cff92a08aadf
Revises: fc1d60a55294
Create Date: 2024-09-17 21:17:26.401298

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cff92a08aadf'
down_revision = 'fc1d60a55294'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=300), nullable=False))
        batch_op.drop_column('password_bash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_bash', mysql.VARCHAR(length=300), nullable=False))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
