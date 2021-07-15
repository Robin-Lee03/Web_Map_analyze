import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])   # Latitude 緯度
lon = list(data["LON"])   # Longitude 經度
elev = list(data["ELEV"])     # 海拔高度


# html = """<h4>Volcano information:</h4>
# Height: %s m
# """
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
    # iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+"m", icon=folium.Icon(color=color_produce(el))))


map.add_child(fg)

map.save("Map.html")
