"""empty message

Revision ID: 44549eda1dd4
Revises: d6d577647907
Create Date: 2022-12-17 16:53:41.071663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44549eda1dd4'
down_revision = 'd6d577647907'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart', schema=None) as batch_op:
        batch_op.drop_column('quantity')

    # ### end Alembic commands ###
