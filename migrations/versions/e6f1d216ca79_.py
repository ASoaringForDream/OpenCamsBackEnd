"""empty message

Revision ID: e6f1d216ca79
Revises: cf2ccd98b24b
Create Date: 2023-04-18 10:12:00.412290

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e6f1d216ca79'
down_revision = 'cf2ccd98b24b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('userpic',
               existing_type=mysql.TEXT(),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('userpic',
               existing_type=mysql.LONGTEXT(),
               type_=mysql.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
