import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import math
from sklearn import metrics,preprocessing
import pickle
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

FILENAME = 'saved_regression.sav'
#INPUT_DATASET_FILENAME = "cleaned_encoded_w1_correct.csv"
INPUT_DATASET_FILENAME = "duration_added.csv"

indexes = pd.read_csv("indices.csv")

coeff = {}

headers = ['BusID','LAT1','LON1','Timestamp1','LAT2','LON2','Timestamp2','Angle','Direction-E','Direction-N','Direction-S','Direction-W','i','j','distance','time1','Speed','time2','duration']

dtypes = {'BusID': 'str','LAT1':np.float64,'LON1':np.float64,'Timestamp1':'str','LAT2':np.float64,'LON2':np.float64,'Timestamp2':'str','Angle':np.float64,'Direction-E':np.int32,'Direction-N':np.int32,'Direction-S':np.int32,'Direction-W':np.int32,'i':np.int32,'j':np.int32,'distance':np.float64,'time1':np.float64,'Speed':np.float64,'time2':np.float64,'duration':np.float64}

columns = ["LAT1","LON1","LAT2","LON2","time1", "Direction-E", "Direction-W", "Direction-N", "Direction-S","distance"]
mse = []
coe=[]
models = []

for index,row in indexes.iterrows():
    #df = pd.read_csv(INPUT_DATASET_FILENAME,dtype=dtypes)
    df = pd.read_csv(INPUT_DATASET_FILENAME, skiprows=row.start - 1, nrows=row.end - row.start + 1,names=headers,dtype=dtypes)
    df = df[df['i'] == row.i]
    df = df[df['j'] == row.j]
    df = df.drop(df[df.duration < 0].index,axis=0)
    X = df[columns]
    y = df["duration"]
    model = RandomForestRegressor(max_depth=6,n_jobs=6)
    X['LAT1'] = X['LAT1']/90
    X['LAT2'] = X['LAT2']/90
    X['LON1'] = X['LON1']/180
    X['LON2'] = X['LON2']/180
    X['time1'] = X['time1']/10080
    X['distance'] = X['distance']/1500
    print(X.distance.describe())
    #polynomial_features = PolynomialFeatures(degree=2)
    #X = polynomial_features.fit_transform(X)
    model.fit(X,y)
    #preds = model.predict(X)
    #error = np.sqrt(metrics.mean_squared_error(y, preds))
    #print(model.score(X,y))
    #print(error)
    #mse.append(error)
    models.append({"i": row.i, "j": row.j, "model": model})
pickle.dump(models, open(FILENAME, 'wb'))
