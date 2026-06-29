import pandas as pd
import os

df = pd.read_csv("sdg_goal8_indicators.csv", low_memory=False)

indicators = ['8.5.1', '8.5.2', '8.6.1']
df = df[df['Indicator'].isin(indicators)]

countries = {
    'Republic of Korea': 'Korea',
    'United States of America': 'United States',
    'Türkiye': 'Turkey'
}

df['GeoAreaName'] = df['GeoAreaName'].replace(countries)

allowed_countries = [
    'Australia',
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'Korea',
    'Mexico',
    'Turkey',
    'United States'
]
df = df[df['GeoAreaName'].isin(allowed_countries)]

df = df[
    [
        'Goal',
        'Target',
        'Indicator',
        'SeriesCode',
        'SeriesDescription',
        'GeoAreaCode',
        'GeoAreaName',
        'TimePeriod',
        'Value',
        'Units',
        'Age',
        'Sex',
        'Nature',
        'Observation Status'
    ]
]

df.columns = [
    'goal',
    'target',
    'indicator',
    'series_code',
    'series_description',
    'geo_area_code',
    'geo_area_name',
    'time_period',
    'value',
    'units',
    'age',
    'sex',
    'nature',
    'observation_status'
]

df['time_period'] = pd.to_numeric(df['time_period'], errors='coerce')
df['value'] = pd.to_numeric(df['value'], errors='coerce')

df = df.dropna(subset=['time_period', 'value'])
df = df.drop_duplicates()
df = df.sort_values(['indicator', 'geo_area_name', 'time_period']).reset_index(drop=True)

os.makedirs("../processed", exist_ok=True)
df.to_csv("../processed/sdg_goal8_indicators.csv", index=False)

print(f"Done. Shape: {df.shape}")
print(df['indicator'].value_counts())
print(df['geo_area_name'].value_counts())
print(df.head(3))
