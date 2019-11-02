import pandas as pd
import numpy as np

large_frame = pd.read_csv("../dataset/w1.csv", chunks=10000000)
count = 0
with open("../dataset/cleaned_w1.csv", "a") as f:
    for df in large_frame:
        print (count)
        df['unique'] = pd.Series(0, index=df.index)
        unique_rows = df.drop_duplicates(subset=['BusID', 'LAT', 'LON', 'Angle', 'Speed'])

        indices = []
        for i,j in unique_rows.iterrows():
            indices.append(i)
            if (i > 0):
                indices.append(i-1)    
        for index in indices:
            df.set_value(index, 'unique', 1)

        df.drop(df[df['unique'] == 0].index, inplace=True)
        df.to_csv(f, header=False, index=False)
        count += 1