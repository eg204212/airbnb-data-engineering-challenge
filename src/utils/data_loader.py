import pandas as pd


def load_csv(path):

    print(f"Loading {path}")

    df = pd.read_csv(
        path,
        low_memory=False
    )

    print(
        f"Rows: {df.shape[0]}"
    )

    print(
        f"Columns: {df.shape[1]}"
    )

    return df