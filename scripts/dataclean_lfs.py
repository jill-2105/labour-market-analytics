import pandas as pd
import os

df = pd.read_csv("lfs_employment_by_industry.csv", low_memory=False)

df = df[['REF_DATE', 'GEO', 'North American Industry Classification System (NAICS)', 'Statistics', 'Data type', 'VALUE']]

df.columns = ['ref_date', 'geo', 'naics', 'statistics', 'data_type', 'value']

df = df.dropna(subset=['value'])

os.makedirs("../processed", exist_ok=True)
df.to_csv("../processed/lfs_employment_by_industry.csv", index=False)

print(f"Done. Shape: {df.shape}")
print(df.head(3))
