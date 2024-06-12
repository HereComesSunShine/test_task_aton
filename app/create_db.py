import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             Name TEXT UNIQUE,
             login TEXT,
             password TEXT)"""
)


c.execute(
    """CREATE TABLE IF NOT EXISTS clients (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             acc_number INTEGER,
             Surname TEXT,
             Name TEXT,
             F_name TEXT,
             Birth_date DATE,
             INN TEXT,
             Manager TEXT,
             Status TEXT DEFAULT 'Не в работе',
             FOREIGN KEY (Manager) REFERENCES users(Name))"""
)

conn.commit()
conn.close()
