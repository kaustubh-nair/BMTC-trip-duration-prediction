import pandas as pd
import numpy as np

#dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.int32, 'Speed': np.int32, 'Timestamp': 'str'}
df = pd.read_csv("../../dataset/small_tail.csv", chunksize=3000000)

with open("../../dataset/time_converted.csv", "a") as f:
    #f.write("BusID,LAT,LON,Angle,Speed,Timestamp,Day,Hour,Minutes,Seconds,Time\n")
    for chunk in df:
        chunk["Day"] = pd.to_numeric(chunk["Timestamp"].astype(str).str[8:10])%7
        hour = pd.to_numeric(chunk["Timestamp"].astype(str).str[11:13])
        minute = pd.to_numeric(chunk["Timestamp"].astype(str).str[14:16])
        second = pd.to_numeric(chunk["Timestamp"].astype(str).str[17:139])
        chunk["Time1"] = (hour*3600) + (minute*60) + (second)

        chunk["Day"] = pd.to_numeric(chunk["Timestamp2"].astype(str).str[8:10])%7
        hour = pd.to_numeric(chunk["Timestamp2"].astype(str).str[11:13])
        minute = pd.to_numeric(chunk["Timestamp2"].astype(str).str[14:16])
        second = pd.to_numeric(chunk["Timestamp2"].astype(str).str[17:139])
        chunk["Time2"] = (hour*3600) + (minute*60) + (second)

        chunk.to_csv(f, header=False, index=False,float_format="%.6f")
