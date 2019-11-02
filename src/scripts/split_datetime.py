import pandas as pd
import numpy as np

dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.int32, 'Speed': np.int32, 'Timestamp': 'str'}
df = pd.read_csv("../dataset/w1.csv", chunksize=3000000,dtype=dtypes)


with open("../dataset/w1_split_datetime.csv", "a") as f:
    f.write("BusID,LAT,LON,Angle,Speed,Timestamp,uniquecolumn,year,month,day,hour,minute,second\n")

    for chunk in df:
        chunk["Year"] = chunk["Timestamp"].astype(str).str[0:4]
        chunk["Month"] = chunk["Timestamp"].astype(str).str[5:7]
        chunk["Day"] = chunk["Timestamp"].astype(str).str[8:10]
        chunk["Hour"] = chunk["Timestamp"].astype(str).str[11:13]
        chunk["Minute"] = chunk["Timestamp"].astype(str).str[14:16]
        chunk["Second"] = chunk["Timestamp"].astype(str).str[17:19]
        chunk.to_csv(f, header=False, index=False,float_format="%.6f")
