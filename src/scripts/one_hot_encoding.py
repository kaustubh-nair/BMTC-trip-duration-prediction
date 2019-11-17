import pandas as pd
import numpy as np
import math


large = pd.read_csv("../../dataset/Sorted/removed_duplicates/pairwise_dataset.csv", chunksize=1000000)

i = 0
with open("../../dataset/Sorted/removed_duplicates/cleaned_encoded_w1.csv", "a") as f:
    f.write("BusID,LAT1,LON1,Timestamp1,LAT2,LON2,Timestamp2,Angle,Direction-E,Direction-N,Direction-S,Direction-W,\n")
    for df in large:
        df.columns = ["BusID","LAT1","LON1", "Timestamp1", "LAT2", "LON2", "Timestamp2", "Angle", "Direction"]
        df = pd.get_dummies(df, columns = ["Direction"])
        df.to_csv(f, header=False, index=False)
        print (i)
        i +=1
