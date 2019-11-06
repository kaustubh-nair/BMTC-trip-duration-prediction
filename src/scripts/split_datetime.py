import pandas as pd
import numpy as np

dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.int32, 'Speed': np.int32, 'Timestamp': 'str','temp': np.int32}
df = pd.read_csv("../dataset/small.csv", chunksize=3000000,dtype=dtypes)


with open("../dataset/small_split_datetime.csv", "a") as f:
    f.write("BusID,LAT,LON,Angle,Speed,Timestamp,year,month,day,hour,minute,second\n")

    for chunk in df:
        print(chunk)
        chunk = chunk.drop(['temp'],axis=1)
        print(chunk)
        chunk["Year"] = chunk["Timestamp"].astype(str).str[0:4]
        chunk["Month"] = chunk["Timestamp"].astype(str).str[5:7]
        chunk["Day"] = chunk["Timestamp"].astype(str).str[8:10]
        chunk["Hour"] = chunk["Timestamp"].astype(str).str[11:13]
        chunk["Minute"] = chunk["Timestamp"].astype(str).str[14:16]
        chunk["Second"] = chunk["Timestamp"].astype(str).str[17:19]
        chunk.to_csv(f, header=False, index=False,float_format="%.6f")
