import pandas as pd
import numpy as np

zerovalues = [0, 0, 0]

df = pd.read_csv("../dataset/w1.csv.sorted", chunksize=3000000)

for chunk in df:
    df_filtered = chunk[chunk['LAT'] != 0]
    df_filtered = df_filtered[df_filtered['LON'] != 0]
    df_filtered = df_filtered[df_filtered['LON'] < 78.2]
    df_filtered = df_filtered[df_filtered['LAT'] < 13.4]
    df_filtered = df_filtered[df_filtered['LAT'] > 12.6]
    df_filtered = df_filtered[df_filtered['LON'] > 76.98]
    df_filtered = df_filtered[df_filtered['Angle'] < 360]
    df_filtered = df_filtered[df_filtered['Angle'] > 0]
    df_filtered = df_filtered[df_filtered['Speed'] < 200]
    print(df_filtered.size)
    df_filtered.to_csv("../dataset/w1_nonzero.csv",mode='a',index=False,header=False)
