import pandas as pd

df = pd.read_csv(r'C:\Users\Андрей\Downloads\flights_NY.csv')

df_clean = df[['tailnum', 'distance', 'air_time']].dropna()

df_clean = df_clean[df_clean['air_time'] > 0]

df_clean['speed'] = df_clean['distance'] * 60 / df_clean['air_time']

df_clean = df_clean[(df_clean['speed'] >= 100) & (df_clean['speed'] <= 700)]

aircraft_stats = df_clean.groupby('tailnum').agg(
    num_flights=('speed', 'count'),   
    avg_speed=('speed', 'mean')       
).reset_index()

aircraft_stats = aircraft_stats[aircraft_stats['num_flights'] >= 10]

aircraft_stats.to_csv('flights_speed_flnum.csv', index=False, float_format='%.10f')

print("Успех")