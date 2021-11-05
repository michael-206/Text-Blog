"""posts table

Revision ID: 9a0959f666bd
Revises: 18246e807375
Create Date: 2021-10-31 12:25:29.480066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a0959f666bd'
down_revision = '18246e807375'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Post', sa.Column('author', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Post', 'author')
    # ### end Alembic commands ###
