import sqlglot
from typing import Tuple, Set

DISALLOWED = {"update","delete","drop","alter","create","replace","attach","detach","truncate","pragma","vacuum","merge"}
ALLOWED_STATEMENTS = {"select","insert"}

def extract_tables(sql: str) -> Set[str]:
    try:
        parsed = sqlglot.parse_one(sql, read="sqlite")
    except Exception:
        return set()
    tables = {t.name for t in parsed.find_all(sqlglot.exp.Table)}
    return tables

def validate_sql(sql: str, allowed_tables: Set[str]) -> Tuple[bool, str]:
    if ";" in sql:
        return False, "semicolon or multiple statements not allowed"
    low = sql.lower()
    for kw in DISALLOWED:
        if f" {kw} " in f" {low} ":
            return False, f"disallowed keyword: {kw}"
    try:
        parsed = sqlglot.parse_one(sql, read="sqlite")
    except Exception as e:
        return False, f"sql parse error: {e}"
    if parsed.key.lower() not in ALLOWED_STATEMENTS:
        return False, "only SELECT statements allowed"
    tables = extract_tables(sql)
    if not tables.issubset(allowed_tables):
        return False, f"disallowed tables used: {tables - allowed_tables}"
    return True, "ok"
