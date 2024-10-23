"""Update del long de la password

Revision ID: 58040e0baba9
Revises: 
Create Date: 2024-09-03 20:59:21.281913

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '58040e0baba9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    op.drop_table('almacen')
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=False)

    op.create_table('almacen',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('stock',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('cantidad_disponible', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('equipo_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('almacen_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['almacen_id'], ['almacen.id'], name='stock_ibfk_1'),
    sa.ForeignKeyConstraint(['equipo_id'], ['equipo.id'], name='stock_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
