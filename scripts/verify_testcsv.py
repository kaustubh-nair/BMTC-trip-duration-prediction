import pandas as pd
import numpy as np

df = pd.read_csv('../dataset/final_bmtc_test_data.csv')

i = 0
print(df)
for index, row in df.iterrows():
    coord = []
    j = 1
    while j < 101:
        a = []
        lat = row["LATLONG"+str(j)].split(":")[0]
        lon = row["LATLONG"+str(j)].split(":")[1]
        a.append([lat,lon])
        if a not in coord:
            coord.append(a)
        j+=1
    i += 1
    print(row["BusId"],len(coord))
