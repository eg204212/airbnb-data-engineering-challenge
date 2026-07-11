from src.utils.data_loader import load_csv
from src.profiling.profiler import profile_dataframe, save_report

from src.validation.validate import (
    check_duplicates,
    check_missing_values,
    validate_price,
    validate_coordinates,
    detect_price_outliers
)

LISTINGS_PATH = "data/raw/extracted/listings.csv"


def main():

    listings = load_csv(LISTINGS_PATH)

    profile = profile_dataframe(
        listings,
        "listings"
    )

    save_report(
        profile,
        "listings_profile.csv"
    )

    check_duplicates(listings)

    missing = check_missing_values(listings)

    missing.to_csv(
        "data/reports/missing_values.csv"
    )

    prices = validate_price(listings)

    validate_coordinates(listings)

    detect_price_outliers(prices)


if __name__ == "__main__":
    main()