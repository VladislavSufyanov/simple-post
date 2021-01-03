from sqlalchemy.sql.schema import Table


class CRUD:

    def __init__(self, table: Table):
        self.table = table
