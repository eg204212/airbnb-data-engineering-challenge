from pathlib import Path
import gzip
import shutil


RAW_DIR = Path("data/raw")
EXTRACTED_DIR = Path("data/raw/extracted")


EXTRACTED_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def extract_gzip_files():

    gzip_files = list(RAW_DIR.glob("*.csv.gz"))

    if not gzip_files:
        print("No compressed files found")
        return


    for file in gzip_files:

        output_file = (
            EXTRACTED_DIR /
            file.name.replace(".gz","")
        )

        print(f"Extracting {file.name}")

        with gzip.open(file,"rb") as f_in:
            with open(output_file,"wb") as f_out:
                shutil.copyfileobj(
                    f_in,
                    f_out
                )

        print(
            f"Created {output_file}"
        )


if __name__ == "__main__":

    extract_gzip_files()