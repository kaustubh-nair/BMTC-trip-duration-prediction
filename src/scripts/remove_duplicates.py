import pandas as pd
import numpy as np
import random

dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.int32, 'Speed': np.int32, 'Timestamp': 'str'}
large_frame = pd.read_csv("../dataset/w1.csv", chunksize=3234567,dtype=dtypes)
with open("../dataset/w1_no_duplicates.csv", "a") as f:
# dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.int32, 'Speed': np.int32, 'Timestamp': 'str'}

    f.write("BusID,LAT,LON,Angle,Speed,Timestamp\n")
    x=0
    for df in large_frame:
        print(x)
        unique_rows = df.drop_duplicates(subset=['BusID', 'LAT', 'LON', 'Angle', 'Speed'])

        indices = []
        for i,j in unique_rows.iterrows():
            indices.append(i)
            if (i > 0):
                indices.append(i-1)    
        for index in indices:
            df.set_value(index, 'unique', 1)

        df.drop(df[df['unique'] == 0].index, inplace=True)
        df.drop([ 'unique' ],axis=1,inplace=True)
        print("Removing null", df.shape)
        df.dropna(axis=0, inplace=True)
        print("removed", df.shape)
        df.to_csv(f, header=False, index=False,float_format="%.6f")
        x+=1
