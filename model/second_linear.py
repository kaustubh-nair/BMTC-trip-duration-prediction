import pandas as pd
from sklearn.linear_model import LinearRegression
import random
import numpy as np
import math
from haversine import haversine, Unit

def predict(test,model):
    for index, row in test.iterrows():
        duration = model.predict([ row ])
        test.loc[test.index == index+1,'Time'] = row.Time + duration
        print(row.Time)


dtypes = {'BusID': np.int32, 'lat1': np.float64, 'lon1': np.float64, 'lat1': np.float64, 'lon2': np.float64, 'Time': np.float64 ,'distance': np.float64, 'duration': np.float64}
df = pd.read_csv('../dataset/pairwise_small.csv', dtype=dtypes)
X = df.loc[:,df.columns != 'duration']
y = df.duration
dtypes2 = {'BusID': np.int32, 'lat1': np.float64, 'lon1': np.float64, 'lat1': np.float64, 'lon2': np.float64, 'Time': np.float64 ,'distance': np.float64}

test = pd.read_csv('../dataset/pairwise_test_split.csv', dtype=dtypes2)

model = LinearRegression().fit(X,y)
predict(test,model)

