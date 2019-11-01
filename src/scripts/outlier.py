import pandas as pd
import numpy as np

zerovalues = [0, 0, 0]

df = pd.read_csv("../dataset/small.csv.sorted", chunksize=1000)

for chunk in df:
    print(chunk.size)
    df_filtered = chunk[chunk['LAT'] != 0]
    df_filtered = df_filtered[df_filtered['LON'] != 0]
    print(df_filtered.size)
    df_filtered.to_csv("../dataset/small.csv",mode='a',index=False)
