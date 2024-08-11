"""empty message

Revision ID: 5dfd9f640013
Revises: db5c9f84471f
Create Date: 2024-08-10 23:20:47.183245

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5dfd9f640013'
down_revision = 'db5c9f84471f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cuit', sa.String(length=13), nullable=False))
        batch_op.drop_column('apellido')
        batch_op.drop_column('mail')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mail', mysql.VARCHAR(length=50), nullable=False))
        batch_op.add_column(sa.Column('apellido', mysql.VARCHAR(length=30), nullable=False))
        batch_op.drop_column('cuit')

    # ### end Alembic commands ###
