import sqlite3
import os


def get_db_connection():
    path = os.getenv("DATABASE_PATH", "agenda.db")
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    schema_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "schema.sql")
    )
    with open(schema_path) as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
