import pandas as pd
import os

df = pd.read_csv("oecd_annual_wages.csv", low_memory=False)

df = df[['REF_AREA', 'Reference area', 'TIME_PERIOD', 'OBS_VALUE', 'UNIT_MEASURE', 'PRICE_BASE', 'PAY_PERIOD']]

df.columns = ['country_code', 'country', 'year', 'avg_annual_wage', 'unit', 'price_base', 'pay_period']

df = df.dropna(subset=['avg_annual_wage'])

os.makedirs("../processed", exist_ok=True)
df.to_csv("../processed/oecd_annual_wages.csv", index=False)

print(f"Done. Shape: {df.shape}")
print(df.head(3))
