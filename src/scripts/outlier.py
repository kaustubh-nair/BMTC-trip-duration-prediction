import pandas as pd
import numpy as np

zerovalues = [0, 0, 0, 0, 0]

df = pd.read_csv("small_sorted.csv")
zerocolumns = ["BusID", "LAT", "LON", "Angle", "Speed"]
for j in range(len(df)):
    for k in range(len(zerovalues)):
        if(np.equal(df.loc[j, zerocolumns[k]], 0)):
            zerovalues[k] += 1

print(zerovalues)
