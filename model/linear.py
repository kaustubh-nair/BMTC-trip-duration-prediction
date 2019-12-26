import pandas as pd
from sklearn.linear_model import LinearRegression
import random
import numpy as np
from haversine import haversine, Unit
from helper import convert_to_segments


def load_for_conversion():
    dtypes = {'BusID': np.int32, 'LAT1': np.float32, 'LON1': np.float32, 'Timestamp1': 'str', 'LAT2': np.float32, 'LON2,': np.float32, 'Timestamp2': 'str', 'Angle': np.float32, 'Direction-E': 'str', 'Direction-N': 'str', 'Direction-S': 'str', 'Direction-W': 'str'}
    df = pd.read_csv('../dataset/small.csv', dtype=dtypes)

    i = 0
    #df = df[df['BusID'] == 150814965]
    #df = df.drop(['BusID','Seconds','Minutes','Hour','Angle','Speed','Day','Timestamp'],axis=1)

    df = df.rename(columns={"LAT": "lat1","LON":"lon1"})
    df = convert_latitudes(df)

def train():
    dtypes = {'BusID': np.int32, 'lat1': np.float64, 'lon1': np.float64, 'lat1': np.float64, 'lon2': np.float64, 'time': np.float64, 'time2': np.float64}
    df = pd.read_csv('../dataset/testing/paired/pairwise_small.csv', dtype=dtypes)
    print(df)
    X = df.loc[:,df.columns != 'duration']
    y = df.duration
    model = LinearRegression().fit(X,y)
    test = X.head(1)
    print(test)
    test.lat2 = X.tail(1).lat1.item()
    test.lon2 = X.tail(1).lon1.item()
    test.distance = haversine((test.lat1, test.lon1), (test.lat2, test.lon2))
    print(test)
    print(model.predict(test))

#load_for_conversion()
df = pd.read_csv('../dataset/time_converted.csv')
convert_to_segments(df)
#train()
