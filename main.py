from src.utils.data_loader import load_csv
from src.profiling.profiler import (
    profile_dataframe,
    save_report
)


LISTINGS_PATH = (
"data/raw/extracted/listings.csv"
)


if __name__ == "__main__":


    listings = load_csv(
        LISTINGS_PATH
    )


    report = profile_dataframe(
        listings,
        "listings"
    )


    save_report(
        report,
        "listings_profile.csv"
    )