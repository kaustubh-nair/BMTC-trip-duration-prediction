import pandas as pd
import numpy as np

df = pd.read_csv("small_sorted.csv")

for i in range(1, len(df)):
    if(np.equal(df.loc[i, "BusID"], df.loc[i+1, "BusID"])) and (np.equal(df.loc[i, "BusID"], df.loc[i-1, "BusID"])):
        j = df[((df.BusID == df.loc[i, "BusID"]))].index
        df.drop(j)
