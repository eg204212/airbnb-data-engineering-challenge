import pandas as pd

# Clean the Price Column
def clean_price(df):

    print("=" * 50)
    print("Cleaning Price Column")
    print("=" * 50)

    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    return df

# Remove Invalid Price

def remove_invalid_prices(df):

    before = len(df)

    df = df[
        (df["price"] > 0)
        &
        (df["price"].notna())
    ]

    after = len(df)

    print(f"Removed {before-after} invalid price records")

    return df

# Remove Invalid Coordinates

def handle_missing_values(df):

    print("=" * 50)
    print("Handling Missing Values")
    print("=" * 50)

    if "reviews_per_month" in df.columns:
        df["reviews_per_month"] = (
            df["reviews_per_month"]
            .fillna(0)
        )

    if "host_response_rate" in df.columns:
        df["host_response_rate"] = (
            df["host_response_rate"]
            .fillna("Unknown")
        )

    return df

# Normalize Room Type
def normalize_room_type(df):

    if "room_type" in df.columns:

        df["room_type"] = (
            df["room_type"]
            .astype(str)
            .str.strip()
            .str.title()
        )

    return df

# Parse Date Columns 

def parse_dates(df):

    date_columns = [

        "host_since",

        "last_review"

    ]

    for col in date_columns:

        if col in df.columns:

            df[col] = pd.to_datetime(

                df[col],

                errors="coerce"

            )

    return df

# Save Cleaned Data

from pathlib import Path

def save_clean_data(df):

    output = Path("data/processed")

    output.mkdir(

        parents=True,

        exist_ok=True

    )

    df.to_csv(

        output / "listings_clean.csv",

        index=False

    )

    print("Clean dataset saved")