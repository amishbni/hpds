import psutil
from database import DatabaseManager
from celery_app import app


class RamUsage:
    DB_NAME = "ram_usage"

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
            ]
        )

    def set_ram_stats(self):
        ram = psutil.virtual_memory()

        self.db.insert(
            self.db_name,
            ["used", "free", "total"],
            [ram.used, ram.free, ram.total],
        )

    def get_ram_stats(self):
        result = self.db.select(self.db_name)
        return result


ram_usage_instance = RamUsage()
