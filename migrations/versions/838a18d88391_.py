"""empty message

Revision ID: 838a18d88391
Revises: 7db8fc8a74c2
Create Date: 2019-01-26 15:46:01.792920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '838a18d88391'
down_revision = '7db8fc8a74c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('rolesid', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'rolesid')
    # ### end Alembic commands ###