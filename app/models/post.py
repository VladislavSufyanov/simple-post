from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from db.db import metadata

from models.utils import utcnow


posts = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id', onupdate='CASCADE', ondelete='SET NULL'), nullable=True),
    Column('date_pub', DateTime(timezone=True), nullable=False, server_default=utcnow()),
    Column('title', String(70), nullable=False),
    Column('text', String(350), nullable=False)
)
