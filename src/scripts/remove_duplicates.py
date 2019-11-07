import pandas as pd
import numpy as np

dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.int32, 'Speed': np.int32, 'Timestamp': 'str'}
large_frame = pd.read_csv("../dataset/small.csv", chunksize=3000000,dtype=dtypes)
with open("../dataset/cleaned_small.csv", "a") as f:
# dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.int32, 'Speed': np.int32, 'Timestamp': 'str'}

    # f.write("BusID,LAT,LON,Angle,Speed,Timestamp\n")
    for df in large_frame:
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
        print (df.size)
        df.to_csv(f, header=False, index=False)
