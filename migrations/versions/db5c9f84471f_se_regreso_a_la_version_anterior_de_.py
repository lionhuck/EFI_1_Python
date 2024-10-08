"""se regreso a la version anterior de celulares.py

Revision ID: db5c9f84471f
Revises: 54c8aa13410c
Create Date: 2024-08-09 14:41:09.859537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db5c9f84471f'
down_revision = '54c8aa13410c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('caracteristica', schema=None) as batch_op:
        batch_op.add_column(sa.Column('descripcion', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('caracteristica', schema=None) as batch_op:
        batch_op.drop_column('descripcion')

    # ### end Alembic commands ###
