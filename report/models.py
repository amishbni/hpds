import psutil
from database import DatabaseManager


class RamUsage:
    DB_NAME = "ram_usage"
    DEFAULT_LIMIT = 10

    def __init__(self, db_name=None):
        self.db_name = db_name or self.DB_NAME
        self.db = DatabaseManager(self.db_name)
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        self.db.create_table(
            self.db_name,
            [
                "id integer primary key autoincrement",
                "used integer not null",
                "free integer not null",
                "total integer not null",
                "created datetime default current_timestamp",
            ]
        )

    def drop_table_if_exists(self):
        self.db.drop_table(self.db_name)

    def set_ram_stats(self):
        ram = psutil.virtual_memory()

        self.db.insert(
            self.db_name,
            ["used", "free", "total"],
            [ram.used, ram.free, ram.total],
        )

    def get_ram_stats(self, limit=DEFAULT_LIMIT):
        result = self.db.select(self.db_name, sort_by="-created", limit=limit)
        return result


ram_usage_instance = RamUsage()
