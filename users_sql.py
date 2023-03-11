"""Creating users SQLite database"""
import sqlite3

conn = sqlite3.connect("users.sql")

conn.execute(
    """CREATE TABLE users
                (username TEXT NOT NULL,
                password TEXT NOT NULL);"""
)
