import folium
import pandas as pd
import numpy as np

dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.float32, 'Speed': np.float32, 'Timestamp': 'str'}
df = pd.read_csv('../dataset/pairwise_small.csv', dtype=dtypes)

i = 0
mapit = folium.Map(location=[12.9716, 77.5946], zoom_start=12, prefer_canvas=True)
print(df)
for index, row in df.iterrows():
    #print(row['LAT'], row['LON'])
    folium.CircleMarker(location=[row['lat1'], row['lon1']], fill_color='#43d9de', radius=2, weight=2).add_to(mapit)
    i += 1
mapit.save('map.html')
