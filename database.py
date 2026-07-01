import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.path.join(os.path.dirname(__file__), "conversations.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id  TEXT NOT NULL,
            role        TEXT NOT NULL,
            content     TEXT NOT NULL,
            timestamp   DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_session
        ON messages (session_id)
    """)
    conn.commit()
    cursor.close()
    conn.close()


def save_message(session_id, role, content):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
            (session_id, role, content)
        )
        conn.commit()
        cursor.close()
    finally:
        conn.close()


def get_messages(session_id, limit=20):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT role, content FROM messages
            WHERE session_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
            """,
            (session_id, limit)
        )
        rows = cursor.fetchall()
        cursor.close()
        return list(reversed([{"role": r[0], "content": r[1]} for r in rows]))
    finally:
        conn.close()
