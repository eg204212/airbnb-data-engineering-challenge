import pandas as pd

# check duplicates 

def check_duplicates(df):

    duplicate_rows = df.duplicated().sum()

    print("=" * 50)
    print("Duplicate Check")
    print("=" * 50)

    print(f"Duplicate rows : {duplicate_rows}")

    return duplicate_rows

# Check missing values 

def check_missing_values(df):

    print("=" * 50)
    print("Missing Values")
    print("=" * 50)

    missing = (
        df
        .isnull()
        .sum()
        .sort_values(ascending=False)
    )

    missing_percent = (
        df
        .isnull()
        .mean()
        * 100
    ).round(2)

    report = pd.DataFrame({

        "Missing Values": missing,

        "Missing %": missing_percent

    })

    print(report.head(20))

    return report

# Invalid Price Check

def validate_price(df):

    print("=" * 50)
    print("Price Validation")
    print("=" * 50)

    prices = (

        df["price"]

        .astype(str)

        .str.replace("$", "", regex=False)

        .str.replace(",", "", regex=False)

    )

    prices = pd.to_numeric(

        prices,

        errors="coerce"

    )

    invalid = prices.isna().sum()

    negative = (prices < 0).sum()

    zero = (prices == 0).sum()

    print(f"Invalid : {invalid}")

    print(f"Negative : {negative}")

    print(f"Zero : {zero}")

    return prices

# Latitude & Longitude Validation

def validate_coordinates(df):

    print("=" * 50)
    print("Coordinate Validation")
    print("=" * 50)

    invalid_lat = (

        (df["latitude"] < -90)

        |

        (df["latitude"] > 90)

    ).sum()

    invalid_lon = (

        (df["longitude"] < -180)

        |

        (df["longitude"] > 180)

    ).sum()

    print(

        f"Invalid Latitude : {invalid_lat}"

    )

    print(

        f"Invalid Longitude : {invalid_lon}"

    )
    
    # Outlier Detection
    
def detect_price_outliers(prices):

    print("=" * 50)
    print("Price Outliers")
    print("=" * 50)

    Q1 = prices.quantile(0.25)

    Q3 = prices.quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR

    upper = Q3 + 1.5 * IQR

    outliers = (

        (prices < lower)

        |

        (prices > upper)

    ).sum()

    print(f"Outliers : {outliers}")