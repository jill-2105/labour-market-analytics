import pandas as pd
from sqlalchemy import create_engine

# Connection
DB_USER = "postgres"
DB_PASS = "toor"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "labour_market_db"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load all 4 CSV
datasets = {
    "lfs_employment":   "lfs_employment_by_industry.csv",
    "seph_earnings":    "seph_earnings_by_industry.csv",
    "oecd_wages":       "oecd_annual_wages.csv",
    "sdg_indicators":   "sdg_goal8_indicators.csv"
}

for table_name, filename in datasets.items():
    df = pd.read_csv(filename)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Loaded {filename} → table '{table_name}' ({len(df)} rows)")

print("\nAll tables loaded successfully!")
