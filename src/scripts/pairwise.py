import pandas as pd
import numpy as np
import math

df = pd.read_csv("cleanset.csv")

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
    if(angle <=45 and angle > 315):
        return 'E'
    if(angle >45 and angle <= 135):
        return 'N'
    if(angle > 135 and angle <= 225):
        return 'W'
    if(angle >225 and angle <= 315):
        return 'S'

for i in range(len(df)-1):
    df.loc[i, "LAT2"] = df.loc[i+1, "LAT1"]
    df.loc[i, "LON2"] = df.loc[i+1, "LON1"]
    df.loc[i, "Timestamp2"] = df.loc[i+1, "Timestamp1"]
    df.loc[i, "Angle"] = angleFromCoordinate(df.loc[i, "LAT1"], df.loc[i, "LON1"], df.loc[i, "LAT2"], df.loc[i, "LON2"])
    df.loc[i, "Direction"] = calculateDirection(df.loc[i, "Angle"])

df = df.head(len(df)-1)

with open("pairwise_dataset.csv", "a") as f:
    f.write("BusID,LAT1,LON1,Timestamp1,LAT2,LON2,Timestamp2,Angle,Direction\n")
    df.to_csv(f, header=False, index=False,float_format="%.6f")
