"""empty message

Revision ID: 094bbaa5e99f
Revises: 
Create Date: 2023-03-02 20:22:25.815787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '094bbaa5e99f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('facts')
    # ### end Alembic commands ###
