import duckdb
import pandas as pd

def load(df: pd.DataFrame):
    con = duckdb.connect("data/warehouse.duckdb")
    con.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id VARCHAR,
            name VARCHAR,
            current_price DOUBLE,
            market_cap DOUBLE,
            price_change_percentage_24h DOUBLE,
            last_updated TIMESTAMP,
            cap_category VARCHAR
        )
    """)

    con.execute("INSERT INTO crypto_prices SELECT * FROM df") 
    print(f"✅ Cargados {len(df)} registros en DuckDB")
    con.close()