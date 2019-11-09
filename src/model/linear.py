import pandas as pd
from sklearn.linear_model import LinearRegression
import random
import numpy as np

def convert_latitudes(df):
    i = 0
    df['lat2'] = 0
    df['lon2'] = 0
    df['time2'] = 0
    while i < 600:
        df.loc[df.index == i,'lat2'] = df.loc[df.index == i+1,'lat1'].item()
        df.loc[df.index == i,'lon2'] = df.loc[df.index == i+1,'lon1'].item()
        df.loc[df.index == i,'time2'] = df.loc[df.index == i+1,'time'].item()
        print(df.iloc[[i]])
        i+=1
    df = df.head(600)
    df.to_csv('../dataset/pairwise_small.csv', index=False, float_format="%.6f")
    return df

def load_for_conversion():
    dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.float32, 'Speed': np.float32, 'Timestamp': 'str'}
    df = pd.read_csv('../dataset/small.csv', dtype=dtypes)

    i = 0
    df = df[df['BusID'] == 150218000]
    df = df.drop(['BusID','second','minute','hour','Angle','Speed','day','month','year','Timestamp'],axis=1)
    df = df.head(1000)
    time = random.sample(range(10000),1000)
    time.sort()
    df['time'] = time

    df = df.rename(columns={"LAT": "lat1","LON":"lon1"})
    df = convert_latitudes(df)

def train():
    dtypes = {'BusID': np.int32, 'lat1': np.float64, 'lon1': np.float64, 'lat1': np.float64, 'lon2': np.float64, 'time': np.int32, 'time2': np.int32}
    df = pd.read_csv('../dataset/pairwise_small.csv', dtype=dtypes)
    X = df.loc[:,df.columns != 'time2']
    y = df.time2
    model = LinearRegression().fit(X,y)
    test = X.head(1)
    print(test)
    test.lat2 = X.tail(1).lat1.item()
    test.lon2 = X.tail(1).lon1.item()
    print(test)
    print(model.predict(test))

#load_for_conversion()
train()
