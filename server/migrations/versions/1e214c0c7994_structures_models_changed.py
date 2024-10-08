"""Structures models changed

Revision ID: 1e214c0c7994
Revises: 9a78b580375d
Create Date: 2024-10-08 22:00:23.663258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e214c0c7994'
down_revision = '9a78b580375d'
branch_labels = None
depends_on = None


def upgrade():
    # Create a new table with the desired structure
    op.create_table('new_messages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('text', sa.String(length=100), nullable=False),  # Set NOT NULL here
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data from the old table to the new table
    op.execute('INSERT INTO new_messages (id, text, created_at, user_id) SELECT id, text, created_at, user_id FROM messages')

    # Drop the old table
    op.drop_table('messages')

    # Rename the new table to the old table's name
    op.rename_table('new_messages', 'messages')

def downgrade():
    # Implement the reverse logic if you need to downgrade
    pass

