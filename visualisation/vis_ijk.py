import folium
import pandas as pd
import numpy as np

dtypes = {'BusID': np.float32, 'LAT': np.float64, 'LON': np.float64, 'Angle': np.float32, 'Speed': np.float32, 'Timestamp': 'str'}
big_df = pd.read_csv('../dataset/converted_gridcells.csv', chunksize=1000000)

i = 0
mapit = folium.Map(location=[12.9716, 77.5946], zoom_start=12, prefer_canvas=True)
bus = []
for df in big_df:
    #df = df[df['BusID'] == 150814965]
    for index, row in df.iterrows():
        print(row)
        print
        if(row.i == 70 and row.j == 110):
            color = '#d47163'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 71 and row.j == 111):
            color = '#467555'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 72 and row.j == 112):
            color = '#3223ba'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 74 and row.j == 114):
            color = '#80001a'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 75 and row.j == 115):
            color = '#3e8c51'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 76 and row.j == 116):
            color = '#992f8e'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 73 and row.j == 113):
            color = '#23bab5'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 69 and row.j == 109):
            color = '#000000'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 73 and row.j == 114):
            color = '#ba2323'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 78 and row.j == 121):
            color = '#784102'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 77 and row.j == 120):
            color = '#b723ba'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 80 and row.j == 125):
            color = '#b7ba23'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        elif(row.i == 81 and row.j == 128):
            color = '#46784b'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
        else:
            color = '#000000'
            folium.CircleMarker(location=[row['lat1'], row['lon1']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat1']) + ' ' + str(row['lon1']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
            folium.CircleMarker(location=[row['lat2'], row['lon2']],color=color, radius=3, weight=3,label=index).add_child(folium.Popup(str(row['lat2']) + ' ' + str(row['lon2']) + ' ' + str(row.i) + ' ' + str(row.j))).add_to(mapit)
    i += 1
mapit.save('colored_grids.html')
