import sqlite3, re, os
from typing import Tuple, List, Any

SQLITE_PATH = os.getenv("SQLITE_PATH", "sample_db/sample.db")

def open_ro_conn():
    return sqlite3.connect(f"file:{SQLITE_PATH}?mode=ro", uri=True, check_same_thread=False)

def enforce_limit(sql: str, limit: int = 1000) -> str:
    if re.search(r'\blimit\b', sql, re.I):
        return sql
    return f"{sql} LIMIT {limit}"

def execute_sql(sql: str, row_limit: int = 1000, timeout=5.0) -> Tuple[List[str], List[Tuple[Any]]]:
    sql_clean = sql.lstrip().lower()
    if sql_clean.startswith("select"):
        sql = enforce_limit(sql, row_limit)
        conn = open_ro_conn()
        conn.execute(f"PRAGMA busy_timeout = {int(timeout*1000)};")
        cur = conn.cursor()
        cur.execute(sql)
        cols = [c[0] for c in cur.description] if cur.description else []
        rows = cur.fetchmany(row_limit)
        conn.close()
    return cols, rows

    conn = sqlite3.connect(SQLITE_PATH, check_same_thread=False)
    conn.execute(f"PRAGMA busy_timeout = {int(timeout*1000)};")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    affected = cur.rowcount
    conn.close()

    cols = ["rows_affected"]
    rows = [(affected,)]
    return cols, rows


