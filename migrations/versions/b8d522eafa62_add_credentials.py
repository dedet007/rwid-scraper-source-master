"""add credentials

Revision ID: b8d522eafa62
Revises: 821dd60d1e05
Create Date: 2020-04-24 19:19:28.622181

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String)
    password = sa.Column(sa.String)
    role = sa.Column(sa.String)
    authenticated = sa.Column(sa.Boolean)


# revision identifiers, used by Alembic.
revision = 'b8d522eafa62'
down_revision = '821dd60d1e05'
branch_labels = None
depends_on = None


credentials = [
    {
        'role': 'admin',
        'username': 'admin',
        'password': '$pbkdf2-sha256$29000$O0fIWUuJsVYKAeB8b805Zw$9Nru6otB88XTl4BK9jyuKV1frUKMxj9Euz9Jv1NacGo', # admin12345
    },
]


def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    for credential in credentials:
        source = User(
            authenticated=False,
            **credential
        )
        session.add(source)
        session.commit()


def downgrade():
    pass
