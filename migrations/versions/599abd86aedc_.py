"""empty message

Revision ID: 599abd86aedc
Revises: f2009c0100d3
Create Date: 2019-03-06 13:30:31.082277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '599abd86aedc'
down_revision = 'f2009c0100d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_name'), 'categories', ['name'], unique=False)
    op.add_column('companies', sa.Column('category_id', sa.Integer(), nullable=False))
    op.add_column('companies', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'companies', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'companies', type_='foreignkey')
    op.drop_column('companies', 'date_created')
    op.drop_column('companies', 'category_id')
    op.drop_index(op.f('ix_categories_name'), table_name='categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
