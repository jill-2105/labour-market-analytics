import pandas as pd
import os

df = pd.read_csv("seph_earnings_by_industry.csv", low_memory=False)

df = df[['REF_DATE', 'GEO', 'Estimate', 'North American Industry Classification System (NAICS)', 'VALUE']]

df.columns = ['ref_date', 'geo', 'estimate', 'naics', 'value']

df = df.dropna(subset=['value'])

os.makedirs("../processed", exist_ok=True)
df.to_csv("../processed/seph_earnings_by_industry.csv", index=False)

print(f"Done. Shape: {df.shape}")
print(df.head(3))
