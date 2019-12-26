import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import math
from sklearn import metrics

df = pd.read_csv("../../dataset/grid.csv", nwows = , skiprows = )

df["Duration"] = (df["Timestamp2"] - df["Timestamp1"])*60
indexNames  =  df[df["Duration"]<=0].index
df = df.drop(indexNames, inplace = False)

df["Distance"] = df["Distance"] * 1000 #Distance in meters
df["Speed"] = df["Distance"] / df["Duration"] #in m/s

columns = ["LAT1", "LON1", "Timestamp1", "LAT2", "LON2", "Angle", "Distance", "East", "West", "North", "South"]
X = df[columns]
y = df["Speed"]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
model = LinearRegression()
model.fit(train_X, train_y)
preds = model.predict(val_X)
print(np.sqrt(metrics.mean_squared_error(val_y, preds)))

print(model.coef_)
