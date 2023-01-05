"""initial changes

Revision ID: 2414c3fbfae2
Revises: 
Create Date: 2022-12-16 12:41:50.344347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2414c3fbfae2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('zipcode', sa.String(length=30), nullable=False))

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=False)

    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.drop_column('zipcode')

    # ### end Alembic commands ###