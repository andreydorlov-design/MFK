import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv(r'C:\Users\Андрей\Downloads\flights_NY.csv')

numeric_cols = ['year', 'month', 'day', 'dep_time', 'dep_delay',
                'arr_time', 'arr_delay', 'air_time', 'distance']
string_cols = ['carrier', 'tailnum', 'origin', 'dest']

df_clean = df.dropna(subset=numeric_cols + string_cols)

df_clean['speed'] = df_clean['distance'] * 60 / df_clean['air_time']

df_clean = df_clean[(df_clean['speed'] >= 100) & (df_clean['speed'] <= 700)]

grouped = df_clean.groupby('tailnum').agg(
    mean_distance=('distance', 'mean'),
    mean_speed=('speed', 'mean'),
    flight_count=('flight', 'count')
).reset_index()

grouped = grouped[grouped["flight_count"] >= 5]

df_clean2 = df_clean

df_clean2.to_csv('flights_speed_distance.csv', index=False, float_format='%.10f')

print ("Успех")