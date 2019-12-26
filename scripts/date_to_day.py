import pandas as pd
import numpy as np

with pd.option_context('display.precision', 10):
    dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.float32, 'Speed': np.float32, 'Timestamp': 'str'}
    df = pd.read_csv("../dataset/small.csv", chunksize=100000, dtype=dtypes)

    for chunk in df:
        print(chunk)
        chunk["date"] = chunk["Timestamp"].astype(str).str[0:10]
        chunk.to_csv("../dataset/small_date.csv", index=False, mode='a',float_format='%.10f')
