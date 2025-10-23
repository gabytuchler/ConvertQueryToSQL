import sqlite3, os
def allowed_tables_from_db(sqlite_path: str):
    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = [t[0] for t in cur.fetchall()]
    conn.close()
    return set(tables)
