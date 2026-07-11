from pathlib import Path
import os

RAW_DIR = Path("data/raw")

required_files = [
    "listings.csv.gz",
    "calendar.csv.gz",
    "reviews.csv.gz"
]

print("=" * 50)
print("Checking Dataset")
print("=" * 50)

missing = []

for file in required_files:
    path = RAW_DIR / file

    if path.exists():
        size = os.path.getsize(path) / (1024 * 1024)
        print(f"✓ {file} ({size:.2f} MB)")
    else:
        print(f"✗ {file} NOT FOUND")
        missing.append(file)

print()

if len(missing) == 0:
    print("Dataset is ready.")
else:
    print("Missing files:")
    for f in missing:
        print("-", f)