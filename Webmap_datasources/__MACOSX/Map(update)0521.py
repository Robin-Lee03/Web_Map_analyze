import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])   # Latitude 緯度
lon = list(data["LON"])   # Longitude 經度
elev = list(data["ELEV"])     # 海拔高度


def color_produce(elevation):
        if elevation < 1500:
            return 'green'
        elif 1500 <= elevation <= 3000:
            return 'cadetblue'
        else:
            return 'blue'


map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")


for ln, lt, el in zip(lon, lat, elev):

    fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6,popup=str(el)+"m",
    fill_color = color_produce(el),color = "black", fill = True , fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data=(open("world.json",'r',encoding='utf-8-sig').read()),
                            style_function = lambda x: {'fillcolor':'yellow'}))

map.add_child(fg)

map.save("New_Map.html")