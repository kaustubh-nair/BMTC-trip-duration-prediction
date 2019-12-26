import folium
import pandas as pd
import numpy as np

df = pd.read_csv('../dataset/final_bmtc_test_data.csv')

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
        print(lat,lon,row["BusId"])
        # red black grey cyan blue pink
        time = {150220445: "#eb4034", 150811705:"#eb9934",150218073:"#e2eb34",150218420:"#68eb34",150219092:"#34ebeb",150814169:"#345ceb",150220781:"#d934eb"}
        folium.CircleMarker(location=[lat,lon],color=time[row.BusId], radius=3, weight=3).add_to(mapit)
        j+=1
    i += 1
mapit.save('first_bus_test.html')
