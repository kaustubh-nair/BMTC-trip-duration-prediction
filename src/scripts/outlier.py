import pandas as pd
import numpy as np

zerovalues = [0, 0, 0]

df = pd.read_csv("../dataset/small.csv", chunksize=3000000)

for chunk in df:
    df_filtered = chunk[chunk['LAT'] != 0]
    df_filtered = df_filtered[df_filtered['LON'] != 0]
    print(df_filtered.size)
    df_filtered.to_csv("../dataset/w1_nonzero.csv",mode='a',index=False,header=False)
