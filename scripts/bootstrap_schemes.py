from pathlib import Path
import duckdb
import pandas as pd

DB_PATH = Path("portfolio.duckdb")

# TEMP: Use :memory: to test logic without file
def get_connection():
        return duckdb.connect(':memory:')  # No file, pure RAM
    #DB_PATH.touch(exist_ok=True)
    #return duckdb.connect(str(DB_PATH))
    

def main() -> None:
    con = get_connection()
    
    # Create table if it does not exist
    con.execute("""
        CREATE TABLE IF NOT EXISTS schemes (
            scheme_code VARCHAR PRIMARY KEY,
            fund_name   VARCHAR,
            plan        VARCHAR,
            option      VARCHAR
        )
    """)
    
    # Dummy data
    df = pd.DataFrame([
        {"scheme_code": "123456", "fund_name": "HDFC Corporate Bond Fund", "plan": "Growth", "option": "Direct"},
        {"scheme_code": "654321", "fund_name": "SBI Bluechip Fund", "plan": "Growth", "option": "Regular"},
    ])
    
    # Clear and insert
    con.execute("DELETE FROM schemes")
    con.register("schemes_df", df)
    con.execute("INSERT INTO schemes SELECT * FROM schemes_df")
    
    # Query with error handling
    result = con.execute("SELECT COUNT(*) FROM schemes").fetchone()
    if result is None:
        print("Error: Query failed - check if table was created")
        print(con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())
    else:
        count = result[0]
        db_path = Path("portfolio.duckdb").resolve()
        print(f"✅ Loaded {count} schemes into DuckDB at {db_path}")


if __name__ == "__main__":
    main()