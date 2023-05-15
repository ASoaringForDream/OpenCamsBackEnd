"""empty message

Revision ID: 325f555c2c03
Revises: b39560694070
Create Date: 2023-05-15 14:50:34.440203

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '325f555c2c03'
down_revision = 'b39560694070'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('visittime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['cam.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('vidit')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vidit',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cid', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('visittime', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['cam.id'], name='vidit_ibfk_2'),
    sa.ForeignKeyConstraint(['uid'], ['user.id'], name='vidit_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('visit')
    # ### end Alembic commands ###
