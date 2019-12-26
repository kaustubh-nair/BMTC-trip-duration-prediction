import folium
import pandas as pd
import numpy as np

dtypes = {'BusID': np.int32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.float32, 'Speed': np.float32, 'Timestamp': 'str'}
df = pd.read_csv('../dataset/temp.csv', dtype=dtypes)

i = 0
mapit = folium.Map(location=[12.9716, 77.5946], zoom_start=12, prefer_canvas=True)
bus = []
j=0
for index, row in df.iterrows():
    print(index)
    j+=1
    time = {"2016-07-01": "#36693c", "2016-07-02":"#b575ff","2016-07-03":"#757aff","2016-07-04":"#75fffa","2016-07-04":"#ffb459","2016-07-05":"#ff5959","2016-07-06":"#6effad"}
    folium.CircleMarker(location=[row['LAT'], row['LON']],color=time[row.Timestamp[:10]], radius=2.5, weight=2.5,label=index).add_to(mapit)
    #folium.Marker(location=[row['LAT2'], row['LON2']],color="green", radius=3, weight=2,label=index).add_to(mapit)
    #points = [[row['LAT1'], row['LON1']],[row['LAT2'], row['LON2']]]
    #if j %2 == 0 :
       #col = "red"
    #else:
       #col = "blue"
    #folium.PolyLine(points, color=col, weight=4, opacity=1).add_to(mapit)
i += 1
mapit.save('diff_days.html')
