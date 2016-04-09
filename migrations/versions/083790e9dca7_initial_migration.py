"""Initial migration

Revision ID: 083790e9dca7
Revises: None
Create Date: 2016-04-09 10:04:18.734997

"""

# revision identifiers, used by Alembic.
revision = '083790e9dca7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('records', sa.Column('publisher', sa.String(length=1024), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('records', 'publisher')
    ### end Alembic commands ###