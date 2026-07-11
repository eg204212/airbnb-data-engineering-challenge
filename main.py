from src.utils.data_loader import load_csv
from src.profiling.profiler import profile_dataframe, save_report

from src.validation.validate import (
    check_duplicates,
    check_missing_values,
    validate_price,
    validate_coordinates,
    detect_price_outliers
)

from src.cleaning.clean_listings import (
    clean_price,
    remove_invalid_prices,
    handle_missing_values,
    normalize_room_type,
    parse_dates,
    save_clean_data
)

from src.cleaning.cleaning_report import create_cleaning_report

LISTINGS_PATH = "data/raw/extracted/listings.csv"


def main():

    listings = load_csv(LISTINGS_PATH)

    # Profiling
    profile = profile_dataframe(listings, "listings")
    save_report(profile, "listings_profile.csv")

    # Validation
    check_duplicates(listings)

    missing = check_missing_values(listings)
    missing.to_csv("data/reports/missing_values.csv")

    prices = validate_price(listings)

    validate_coordinates(listings)

    detect_price_outliers(prices)

   
    # SAVE ORIGINAL DATAFRAME HERE
   
    original_df = listings.copy()

    # Cleaning
    listings = clean_price(listings)

    listings = remove_invalid_prices(listings)

    listings = handle_missing_values(listings)

    listings = normalize_room_type(listings)

    listings = parse_dates(listings)

    save_clean_data(listings)

    # CREATE CLEANING REPORT HERE
    create_cleaning_report(
        original_df,
        listings
    )


if __name__ == "__main__":
    main()