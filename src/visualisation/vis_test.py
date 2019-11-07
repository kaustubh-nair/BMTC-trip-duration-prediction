import folium
import pandas as pd
import numpy as np

df = pd.read_csv('../dataset/test.csv')

i = 0
mapit = folium.Map(location=[12.9716, 77.5946], zoom_start=12, prefer_canvas=True)
print(df)
for index, row in df.iterrows():
    if(i==7):
        break
    #print(row['LAT'], row['LON'])
    j = 1
    while j < 101:
        lat = row["LATLONG"+str(j)].split(":")[0]
        lon = row["LATLONG"+str(j)].split(":")[1]
        print(lat,lon,row["Id"])
        # red black grey cyan blue pink
        bus = {150220445: "#eb4034", 150811705:"#000d09",150218073:"#e2eb34",150218420:"#7d7d7d",150219092:"#34ebeb",150814169:"#345ceb",150220781:"#d934eb"}
        folium.CircleMarker(location=[lat,lon], color=bus[row["Id"]], radius=2, weight=2).add_to(mapit)
        j+=1
    i += 1
mapit.save('first_six_buses_test.html')
