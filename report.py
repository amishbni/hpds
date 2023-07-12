import psutil
import sqlite3

DB_NAME = "ram_usage"
db = sqlite3.connect(f"{DB_NAME}.db")
cursor = db.cursor()

create_table = (
    f'create table if not exists {DB_NAME} '
    '(id integer primary key autoincrement, '
    'free integer not null, '
    'available integer not null, '
    'used integer not null, '
    'total integer not null);'
)

insert_query = f'insert into {DB_NAME} (free, available, used, total) values (?, ?, ?, ?)'

cursor.execute(create_table)

ram = psutil.virtual_memory()

cursor.execute(insert_query, (ram.free, ram.available, ram.used, ram.total))
