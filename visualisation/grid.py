import folium
import pandas as pd
import numpy as np

big_df = pd.read_csv('../dataset/grid.csv', chunksize=1000000)

i = 0
mapit = folium.Map(location=[12.9716, 77.5946], zoom_start=12, prefer_canvas=True)
bus = []
bounds = [(12.8,76.98),(12.8,78.98),(14.8,76.98),(14.8,78.98)]
folium.Rectangle(bounds).add_to(mapit)
#   for df in big_df:
#       #df = df[df['BusID'] == 150814965]
#       for index, row in df.iterrows():
#           #time = {"2016-07-01": "#eb4034", "2016-07-02":"#eb9934","2016-07-03":"#e2eb34","2016-07-04":"#68eb34","2016-07-04":"#34ebeb","2016-07-05":"#345ceb","2016-07-06":"#d934eb"}
#           folium.CircleMarker(location=[row['LAT1'], row['LON1']], radius=3, weight=3,label=index).add_to(mapit)
#           folium.CircleMarker(location=[row['LAT2'], row['LON2']], radius=3, weight=3,label=index).add_to(mapit)
#       i += 1
mapit.save('grid.html')
