import sqlglot
from typing import Tuple, Set
from sqlglot import exp

ALLOWED_STATEMENTS = {"select", "insert"}
DISALLOWED_STATEMENT_KEYS = {
    "update", "delete", "drop", "alter", "create", "replace",
    "attach", "detach", "truncate", "pragma", "vacuum", "merge"
}

def extract_tables(parsed: exp.Expression) -> Set[str]:
    return {t.name for t in parsed.find_all(exp.Table) if t.name}

def validate_sql(sql: str, allowed_tables: Set[str]) -> Tuple[bool, str]:
    if ";" in sql:
        return False, "semicolon or multiple statements not allowed"

    try:
        parsed = sqlglot.parse_one(sql, read="sqlite")
    except Exception as e:
        return False, f"sql parse error: {e}"

    stmt_key = (parsed.key or "").lower()
    if stmt_key in DISALLOWED_STATEMENT_KEYS:
        return False, f"disallowed statement: {stmt_key}"
    if stmt_key not in ALLOWED_STATEMENTS:
        return False, f"only {sorted(ALLOWED_STATEMENTS)} statements allowed"

    dangerous_nodes = (exp.Delete, exp.Update, exp.Drop, exp.Alter, exp.Create, exp.Truncate, exp.Command)
    if any(isinstance(node, dangerous_nodes) for node in parsed.walk()):
        return False, "disallowed operation detected"

    tables = extract_tables(parsed)
    if not tables.issubset(allowed_tables):
        return False, f"disallowed tables used: {sorted(tables - allowed_tables)}"

    if isinstance(parsed, exp.Insert):
        if parsed.expression is not None:
            return False, "INSERT ... SELECT is not allowed (VALUES only)"
        if parsed.args.get("source") is None:
            return False, "INSERT must use VALUES"

    return True, "ok"
