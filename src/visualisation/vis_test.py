import folium
import pandas as pd
import numpy as np

df = pd.read_csv('../dataset/test.csv')

i = 0
mapit = folium.Map(location=[12.9716, 77.5946], zoom_start=12, prefer_canvas=True)
print(df)
for index, row in df.iterrows():
    #print(row['LAT'], row['LON'])
    j = 1
    while j < 101:
        print("ASD")
        lat = row["LATLONG"+str(j)].split(":")[0]
        lon = row["LATLONG"+str(j)].split(":")[1]
        print(lat,lon)
        folium.CircleMarker(location=[lat,lon], fill_color='#43d9de', radius=2, weight=2).add_to(mapit)
        j+=1
    i += 1
    if(i==3):
        break
mapit.save('a.html')
