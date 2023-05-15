"""empty message

Revision ID: b39560694070
Revises: 404183da1b0f
Create Date: 2023-05-15 13:09:59.687439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b39560694070'
down_revision = '404183da1b0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('collect', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['uid'], ['id'])
        batch_op.create_foreign_key(None, 'cam', ['cid'], ['id'])

    with op.batch_alter_table('dislikeed', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['uid'], ['id'])
        batch_op.create_foreign_key(None, 'cam', ['cid'], ['id'])

    with op.batch_alter_table('likeed', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['uid'], ['id'])
        batch_op.create_foreign_key(None, 'cam', ['cid'], ['id'])

    with op.batch_alter_table('vidit', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'user', ['uid'], ['id'])
        batch_op.create_foreign_key(None, 'cam', ['cid'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vidit', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('likeed', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('dislikeed', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('collect', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
