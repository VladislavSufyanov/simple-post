from typing import Optional

from sqlalchemy.sql.schema import Table


class CRUD:

    def __init__(self, table: Table, related_tables: Optional[dict] = None):
        self.table = table
        self.related_tables = related_tables
