import sqlalchemy
from db.db import metadata


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String),
    sqlalchemy.Column('password', sqlalchemy.String)
)