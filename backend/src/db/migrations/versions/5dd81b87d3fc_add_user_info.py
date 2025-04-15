"""add user info

Revision ID: 5dd81b87d3fc
Revises: 800d0ba2c022
Create Date: 2025-03-03 11:56:09.193521

"""

import sqlalchemy as sa
from alembic import op

revision = "5dd81b87d3fc"
down_revision = "800d0ba2c022"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "telegram_bot",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("telegram_id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id"),
        sa.UniqueConstraint("user_id"),
    )
    op.add_column("user", sa.Column("name", sa.String(), nullable=True))
    op.add_column("user", sa.Column("email", sa.String(), nullable=True))
    op.add_column("user", sa.Column("telegram_id", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "telegram_id")
    op.drop_column("user", "email")
    op.drop_column("user", "name")
    op.drop_table("telegram_bot")
    # ### end Alembic commands ###
