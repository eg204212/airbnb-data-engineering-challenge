from src.ingestion.extract_data import extract_gzip_files
from src.warehouse.build_database import build_database

print("Running complete pipeline...")

extract_gzip_files()

build_database()

print("Pipeline completed.")