from pathlib import Path
import duckdb

DB_PATH = Path("portfolio.duckdb")

def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Return a DuckDB connection to the main portfolio database.
    """
    DB_PATH.touch(exist_ok=True)
    return duckdb.connect(str(DB_PATH))
