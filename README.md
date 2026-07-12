# Airbnb Data Engineering Pipeline

## Overview
Production-ready Airbnb data engineering pipeline built using Python, Pandas, DuckDB, SQL and Streamlit.

## Features
- Automated data ingestion
- Data profiling and validation
- Data cleaning pipeline
- DuckDB warehouse
- Star schema
- SQL analytics
- Exploratory data analysis
- Interactive Streamlit dashboard

## Tech Stack
Python, Pandas, DuckDB, SQL, Streamlit, Plotly, Matplotlib

## Project Structure
```
src/
data/
database/
sql/
images/
report/
```

## Installation
```bash
pip install -r requirements.txt
```

## Run
```bash
python main.py
streamlit run src/dashboard/app.py
```

## Report

The final write-up is available at [report/final_report.md](report/final_report.md). It is structured to match the assignment sections and can be exported to PDF if needed.

## Dashboard

The project includes an interactive Streamlit dashboard providing:

- Market overview KPIs
- Price distribution analysis
- Room type analysis
- Neighbourhood pricing trends
- Geographic listing visualization

Run:

streamlit run src/dashboard/app.py

## License
MIT








