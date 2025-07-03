import sqlite3
import os

DB_PATH = os.path.join("/tmp", "news.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

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
