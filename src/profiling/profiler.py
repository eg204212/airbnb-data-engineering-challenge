import pandas as pd
from pathlib import Path


def profile_dataframe(df, name):

    report = []


    for column in df.columns:


        report.append({

            "dataset":name,

            "column":column,

            "datatype":
                str(df[column].dtype),

            "rows":
                len(df),

            "missing_values":
                df[column].isna().sum(),

            "missing_percentage":
                round(
                    df[column].isna().mean()*100,
                    2
                ),

            "unique_values":
                df[column].nunique()

        })


    return pd.DataFrame(report)



def save_report(df, filename):

    output = Path(
        "data/reports"
    )

    output.mkdir(
        exist_ok=True
    )


    df.to_csv(
        output / filename,
        index=False
    )


    print(
        "Report saved"
    )