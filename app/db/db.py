from databases import Database
import sqlalchemy

from core.config import settings


db = Database(settings.DATABASE_URL)

metadata = sqlalchemy.MetaData()
