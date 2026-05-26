import pandas as pd

df = pd.read_csv(r'C:\Users\Андрей\Downloads\flights_NY.csv')

numeric_cols = ['year', 'month', 'day', 'dep_time', 'dep_delay',
                'arr_time', 'arr_delay', 'air_time', 'distance']
string_cols = ['carrier', 'tailnum', 'origin', 'dest']

df_clean = df.dropna(subset=numeric_cols + string_cols)

df_ny['delay_flag'] = (df_ny['dep_delay'] > 0).astype(int)

result = df_ny.groupby('carrier').agg(
    unique_planes=('tailnum', 'nunique'),   
    prob_delay=('delay_flag', 'mean')       
).reset_index()

result_filtered = result[result['unique_planes'] > 200].copy()

result_sorted = result_filtered.sort_values('unique_planes', ascending=False)

output_file = 'carrier_summary.csv'
result_sorted.to_csv(output_file, index=False, encoding='utf-8')