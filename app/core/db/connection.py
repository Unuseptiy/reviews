import sqlite3
from ...settings import CommentsSettings

settings = CommentsSettings.load_from_env()


DB_NAME = settings.DB_NAME


CREATION_SQL = """
CREATE TABLE IF NOT EXISTS reviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  sentiment TEXT NOT NULL,
  created_at TEXT NOT NULL
);
"""


def get_connection():
    try:
        connection = sqlite3.connect(DB_NAME)
        yield connection
    finally:
        connection.close()
