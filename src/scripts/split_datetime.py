import pandas as pd
import numpy as np

df = pd.read_csv("../dataset/small.csv")
df["Year"] = df["Timestamp"].astype(str).str[0:4]
df["Month"] = df["Timestamp"].astype(str).str[6:8]
df["Day"] = df["Timestamp"].astype(str).str[10:12]
df["Hour"] = df["Timestamp"].astype(str).str[14:16]
df["Minute"] = df["Timestamp"].astype(str).str[18:20]
df["Second"] = df["Timestamp"].astype(str).str[22:24]
print(df)
