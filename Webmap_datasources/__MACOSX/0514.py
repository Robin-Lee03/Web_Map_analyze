import folium

import pandas

# map = folium.Map(location=[48.23,16.45])
# map.save("Map1.html")
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])


map2 = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")   # zoom_start = 比例尺

fg = folium.FeatureGroup(name="My Map")   #Feature Group = 功能組合包的概念

for ln, lt in zip(lon, lat):
    fg.add_child(folium.Marker(location=[ln,lt], popup="I'm a marker", icon=folium.Icon(color='green')))


map2.add_child(fg)                 # add_child 增加地圖中的funtions

map2.save("Map2.html")