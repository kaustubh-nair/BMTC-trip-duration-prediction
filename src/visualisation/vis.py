import folium
import pandas as pd
import numpy as np

dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.float32, 'Speed': np.float32, 'Timestamp': 'str'}
big_df = pd.read_csv('../dataset/small_tail.csv', dtype=dtypes, chunksize=1000000)

i = 0
mapit = folium.Map(location=[12.9716, 77.5946], zoom_start=12, prefer_canvas=True)
bus = []
for df in big_df:
    for index, row in df.iterrows():
        print(row['Timestamp'])
        time = {"2016-07-01": "#eb4034", "2016-07-02":"#eb9934","2016-07-03":"#e2eb34","2016-07-04":"#68eb34","2016-07-04":"#34ebeb","2016-07-05":"#345ceb","2016-07-06":"#d934eb"}
        folium.CircleMarker(location=[row['LAT'], row['LON']], color=time[row['Timestamp'].split(" ")[0]], radius=2, weight=2,label=index).add_child(folium.Popup(index)).add_to(mapit)
    i += 1
mapit.save('small_tail.html')
