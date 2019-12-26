import pandas as pd
import numpy as np

large_frame = pd.read_csv("../../dataset/Sorted/cleaned_reusable_w1.csv", chunksize=7000000)
save = []
with open("../../dataset/route_150220445.csv", "a") as f:
    for df in large_frame:
        df.columns = ['BusID','LAT', 'LON', 'Angle', 'Speed', 'Timestamp']
        a = df.loc[df['BusID'] == 150220445]
        a.to_csv(f, index=False)        
    