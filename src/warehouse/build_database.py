import duckdb
import pandas as pd
from pathlib import Path

DB_PATH = "database/airbnb.duckdb"

DATA_PATH = "data/processed/listings_clean.csv"


def build_database():

    Path("database").mkdir(exist_ok=True)

    conn = duckdb.connect(DB_PATH)

    df = pd.read_csv(DATA_PATH)

    conn.execute("DROP TABLE IF EXISTS listings")

    conn.register("temp_df", df)

    conn.execute("""

        CREATE TABLE listings AS

        SELECT *

        FROM temp_df

    """)

    print("Database created successfully.")

    conn.close()


if __name__ == "__main__":
    build_database()