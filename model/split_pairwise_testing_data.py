import pandas as pd
from sklearn.linear_model import LinearRegression
import random
import numpy as np
import math
from haversine import haversine, Unit
from helper import insert_row,convert_to_segments

def midpoint(lat1,lat2,lon1,lon2):
   lat1, lat2 = math.radians(lat1), math.radians(lat2)
   lon1, lon2 = math.radians(lon1), math.radians(lon2)
   dlon = lon2 - lon1
   dx = math.cos(lat2) * math.cos(dlon)
   dy = math.cos(lat2) * math.sin(dlon)
   lat3 = math.atan2(math.sin(lat1) + math.sin(lat2), math.sqrt((math.cos(lat1) + dx) * (math.cos(lat1) + dx) + dy * dy))
   lon3 = lon1 + math.atan2(dy, math.cos(lat1) + dx)
   return [math.degrees(lat3), math.degrees(lon3)]

def distance(lat1,lon1,lat2,lon2):
    a = (lat1, lon1)
    b =  (lat2, lon2)
    return haversine(a,b)

def split_coordinates(lat1,lon1,lat2,lon2):
    a = (lat1, lon1)
    b =  (lat2, lon2)
    if distance(lat1,lon1,lat2,lon2) < 0.05:
        return False
    else:
        return midpoint(lat1,lat2,lon1,lon2)

def load_test(df):
    all_false = False
    while(all_false == False):
        all_false = True
        for index, row in df.iterrows():
            print(index)
            a = split_coordinates(row['lat1'],row['lon1'],row['lat2'],row['lon2'])
            print(a)
            if a != False:
                new_row = [a[0],a[1],0, row['lat2'],row['lon2'],distance(a[0],a[1],row['lat2'],row['lon2'])]
                df = insert_row(index+1,df,new_row)
                df.loc[df.index == index,'lat2'] = a[0]
                df.loc[df.index == index,'lon2'] = a[1]
                df.loc[df.index == index,'distance'] = distance(a[0],a[1],row['lat1'],row['lon1'])
                all_false = False
                break
    df.to_csv('../dataset/pairwise_test_split.csv', index=False, float_format="%.6f")

dtypes = {'BusID': np.int32, 'lat1': np.float64, 'lon1': np.float64, 'lat1': np.float64, 'lon2': np.float64, 'time': np.float64, 'time2': np.float64}
df = pd.read_csv('../dataset/testing/train.csv', dtype=dtypes)
df = convert_to_segments(df)

#df = pd.read_csv('../dataset/pairwise_small.csv', dtype=dtypes)
print(np.mean(df['distance']))

