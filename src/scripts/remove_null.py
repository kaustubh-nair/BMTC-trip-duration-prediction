import pandas as pd
import numpy as np
import random

large_frame = pd.read_csv("../dataset/w1.csv", chunksize=1111111)
with open("../dataset/w1_no_null.csv", "a") as f:

    f.write("BusID,LAT,LON,Angle,Speed,Timestamp\n")
    x=0
    for df in large_frame:
        print(x)
        print(df.shape)
        df.dropna(axis=0, inplace=True)
        print(df.shape)
        df.to_csv(f, header=False, index=False,float_format="%.6f")
        x+=1
