import sqlite3

DB_PATH = "news.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # So fetch returns dict-like rows
    return conn

def create_tables():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT NOT NULL,
            source TEXT,
            country TEXT,
            region TEXT,
            topic TEXT
        )
    ''')
    conn.commit()
    conn.close()
