"""Initial client table

Revision ID: 63701b0267d8
Revises: 9769293557ba
Create Date: 2025-06-13 11:21:50.457822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63701b0267d8'
down_revision = '9769293557ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('order_history', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clients')
    # ### end Alembic commands ###
