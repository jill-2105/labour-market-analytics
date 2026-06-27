import pandas as pd
import os

df = pd.read_csv("sdg_goal8_indicators.csv", low_memory=False)

indicators = ['8.5.1', '8.5.2', '8.6.1', '8.8.1', '8.8.2']
df = df[df['Indicator'].isin(indicators)]

countries = ['Canada', 'Australia', 'France', 'Germany', 'Italy', 'Japan', 'Republic of Korea', 'Mexico', 'Türkiye', 'United Kingdom', 'United States of America']
df = df[df['GeoAreaName'].isin(countries)]

df = df[['Goal', 'Target', 'Indicator', 'SeriesCode', 'SeriesDescription', 'GeoAreaCode', 'GeoAreaName', 'TimePeriod', 'Value', 'Units', 'Age', 'Sex', 'Location', 'Nature', 'Observation Status']]

df.columns = ['goal', 'target', 'indicator', 'series_code', 'series_description', 'geo_area_code', 'geo_area_name', 'time_period', 'value', 'units', 'age', 'sex', 'location', 'nature', 'observation_status']

df = df.dropna(subset=['value'])
os.makedirs("../processed", exist_ok=True)
df.to_csv("../processed/sdg_goal8_indicators.csv", index=False)

print(f"Done. Shape: {df.shape}")
print(df['indicator'].value_counts())
print(df['geo_area_name'].value_counts())
print(df.head(3))
