import pandas as pd
from pathlib import Path


def create_cleaning_report(original_df, cleaned_df):

    report = pd.DataFrame({
        "Metric": [
            "Original Rows",
            "Cleaned Rows",
            "Rows Removed"
        ],
        "Value": [
            len(original_df),
            len(cleaned_df),
            len(original_df) - len(cleaned_df)
        ]
    })

    output = Path("data/reports")
    output.mkdir(exist_ok=True)

    report.to_csv(
        output / "cleaning_report.csv",
        index=False
    )

    print("Cleaning report saved")