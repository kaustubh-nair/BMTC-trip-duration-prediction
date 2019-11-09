import pandas as pd
import numpy as np

dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.int32, 'Speed': np.int32, 'Timestamp': 'str'}
df = pd.read_csv("../../dataset/small_tail.csv", chunksize=3000000,dtype=dtypes)

with open("../../dataset/time_converted.csv", "a") as f:
    f.write("BusID,LAT,LON,Angle,Speed,Timestamp,Day,Hour,Minutes,Seconds,Time\n")
    for chunk in df:
        chunk["Day"] = pd.to_numeric(chunk["Timestamp"].astype(str).str[8:10])%7
        chunk["Hour"] = pd.to_numeric(chunk["Timestamp"].astype(str).str[11:13])
        chunk["Minutes"] = pd.to_numeric(chunk["Timestamp"].astype(str).str[14:16])
        chunk["Seconds"] = pd.to_numeric(chunk["Timestamp"].astype(str).str[17:139])
        chunk["Time"] = chunk["Hour"] + chunk["Minutes"]/60 + chunk["Seconds"]/3600

        # chunk.drop(["Timestamp,Day,Hour,Minutes,Seconds"], axis = 1, inplace = True)

        chunk.to_csv(f, header=False, index=False,float_format="%.6f")
