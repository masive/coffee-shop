from typing import Any

from sqlalchemy import text

from db import cursor


def execute_query(query: text) -> list[dict[str, Any]]:
    """Executes a query and returns the result as a list of dictionaries."""
    query_result = cursor.execute(query)
    rows = query_result.fetchall()
    columns = query_result.keys()
    result_as_dicts = [dict(zip(columns, row)) for row in rows]
    query_result.close()
    return result_as_dicts
