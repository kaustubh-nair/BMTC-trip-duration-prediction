import pandas as pd
import numpy as np
import math
import sys
large = pd.read_csv("../../dataset/Sorted/removed_duplicates/cleaned_w1.csv", chunksize=1000000)

def angleFromCoordinate(LAT1, LON1, LAT2, LON2):
    dLon = (LON2 - LON1)
    y = math.sin(dLon) * math.cos(LAT2)
    x = math.cos(LAT1) * math.sin(LAT2) - math.sin(LAT1) * math.cos(LAT2) * math.cos(dLon)
    brng = math.atan2(y, x)
    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    brng = 360 - brng
    return brng

def calculateDirection(angle):
    if(angle <=45 or angle > 315):
        return 'E'
    if(angle >45 and angle <= 135):
        return 'N'
    if(angle > 135 and angle <= 225):
        return 'W'
    if(angle >225 and angle <= 315):
        return 'S'

cs = 1000000
j = 0
with open("../../dataset/Sorted/removed_duplicates/pairwise_dataset.csv", "a") as f:
    
    f.write("BusID,LAT1,LON1,Timestamp1,LAT2,LON2,Timestamp2,Angle,Direction\n")
    for df in large:
        print(df.dtypes)
        df.columns = ["BusID", "LAT1", "LON1","Timestamp1"]
        for i in range(len(df)-1):
            df.at[i + j*cs, "LAT2"] = df.loc[i+j*cs +1, "LAT1"]
            df.at[i + j*cs, "LON2"] = df.loc[i+ + j*cs + 1, "LON1"]
            df.at[i + j*cs, "Timestamp2"] = df.loc[i + j*cs +1, "Timestamp1"]
            df.at[i + j*cs, "Angle"] = angleFromCoordinate(df.loc[i + j*cs, "LAT1"], df.loc[i + j*cs, "LON1"], df.loc[i + j*cs, "LAT2"], df.loc[i + j*cs, "LON2"])
            df.at[i + j*cs, "Direction"] = calculateDirection(df.loc[i+j*cs, "Angle"])
        #df = df.head(len(df)-1)
        df.drop(df.index[len(df)-1], inplace=True)
        df.to_csv(f, header=False, index=False,float_format="%.6f")
        print (j)
        j += 1

