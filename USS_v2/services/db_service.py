import sqlite3
from config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY,
        message TEXT,
        type TEXT
    )''')

    conn.commit()
    conn.close()