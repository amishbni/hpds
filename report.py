import psutil
from database import DatabaseManager


DB_NAME = "ram_usage"
DEFAULT_LIMIT = 10


db = DatabaseManager(DB_NAME)
db.create_table(
    DB_NAME,
    [
        "id integer primary key autoincrement",
        "used integer not null",
        "free integer not null",
        "total integer not null",
    ]
)

ram = psutil.virtual_memory()

db.insert(
    DB_NAME,
    ["used", "free", "total"],
    [ram.used, ram.free, ram.total],
)

result = db.select(DB_NAME, columns=["used", "free", "total"], limit=DEFAULT_LIMIT)
print(result)
