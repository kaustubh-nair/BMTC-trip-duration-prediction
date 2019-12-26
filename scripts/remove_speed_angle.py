import pandas as pd
import numpy as np

large = pd.read_csv("../../dataset/Sorted/removed_duplicates/w1.csv", chunksize=1000000)
with open("../../dataset/Sorted/removed_duplicates/cleaned_w1.csv", "a") as f:
    i = 0
    for df in large:
        df.drop(["Speed", "Angle"], axis=1, inplace=True)
        df.to_csv(f, index=False)
        print (i)
        i+=1
