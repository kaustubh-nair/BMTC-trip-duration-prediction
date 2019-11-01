import pandas as pd
import numpy as np

df = pd.read_csv('../dataset/medium.csv', chunksize=300000)

buses = np.array([])
for data in df:
    buses = np.append(buses, data.BusID.unique())
    sizes = []
    print(np.unique(buses).size)
    for bus in buses:
        rows = data.loc[data['BusID'] == bus]
        sizes.append(rows.size)

print(np.unique(buses).size)
