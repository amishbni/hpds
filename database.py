import sqlite3


class DatabaseManager:
    def __init__(self, database_name):
        self.db = sqlite3.connect(f"{database_name}.db")
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def query(self, query, params=None):
        if params is None:
            result = self.cursor.execute(query)
        else:
            result = self.cursor.execute(query, **params)
        self.db.commit()
        return result

    def create_table(self, table_name, columns):
        query = (
            f"create table if not exists {table_name} "
            f'({", ".join(columns)});'
        )

        self.query(query)

    def drop_table(self, table_name):
        query = (
            f"drop table if exists {table_name};"
        )

        self.query(query)

    def insert(self, table_name, columns, values):
        query = (
            f"insert into {table_name} "
            f'({", ".join(columns)}) '
            f'values ({", ".join(map(str, values))});'
        )

        self.query(query)

    def select(self, table_name, columns=None, sort_by=None, limit=None):
        columns = ", ".join(columns) if columns is not None else "*"
        query = f"select {columns} from {table_name}"

        if sort_by is not None:
            if sort_by.startswith("-"):
                sort_by = sort_by.replace("-", '')
                sort_order = "desc"
            else:
                sort_order = "asc"
            query += f" order by {sort_by} {sort_order}"

        if limit is not None:
            query += f" limit {limit}"

        query += ";"
        return self.query(query).fetchall()
