from scgraph.geographs.marnet import marnet_geograph
import folium

import geopandas as gpd
import json
from shapely.geometry import Point

f = open('ports.json')

# returns JSON object as
# a dictionary
data = json.load(f)
ports_gdf = gpd.GeoDataFrame(data)

# Step 3: Convert latitude and longitude to Point geometry
ports_gdf['geometry'] = ports_gdf.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)

start_coordinates = " 69.66566334594751, 23.23926848297695"

your_point = gpd.GeoDataFrame({'geometry': [Point(start_coordinates.split(',')[0], start_coordinates.split(',')[1])]}, crs=ports_gdf.crs)
nearest_port_index = ports_gdf.distance(your_point.unary_union)
sorted = nearest_port_index.sort_values()
indexes = sorted.iloc[:3].index
print(indexes)
import requests
from pyproj import CRS, Transformer
crs_hk80 = CRS.from_proj4("+proj=tmerc +lat_0=22.31213333333334 +lon_0=114.1785555555556 +k=1 +x_0=836694.05 +y_0=819069.8 +ellps=intl +towgs84=-162.619,-276.959,-161.764,0.067753,-2.24365,-1.15883,-1.09425 +units=m +no_defs ")
transformer = Transformer.from_crs(crs_hk80, 4326)
transformer.transform(835000, 812000)
INTERSECTION_ID = 'Start'
url = "https://api.openrouteservice.org/v2/directions/driving-car"
# api_key = "5b3ce3597851110001cf6248846d6a68ec334aaaa34195cdcd3f11ad"
api_key = "5b3ce3597851110001cf6248bef52906ad594343afbb98f64d4f4fa0"
failed_coords = []
# end_coordinates = "72.963540, 18.952151"
m = folium.Map(location=(start_coordinates.split(',')[1], start_coordinates.split(',')[0]))
folium.Marker((start_coordinates.split(',')[1], start_coordinates.split(',')[0]), tooltip=folium.Tooltip(INTERSECTION_ID, permanent=True)).add_to(m)


ports = []
for i in indexes:
  ports.append((ports_gdf.iloc[i]["Latitude"],ports_gdf.iloc[i]["Longitude"]))
  print(ports_gdf.iloc[i]["Latitude"],ports_gdf.iloc[i]["Longitude"])
  end_coordinates = str(ports_gdf.iloc[i]["Longitude"]) + "," + str(ports_gdf.iloc[i]["Latitude"])
  params = {
      "api_key": api_key,
      "start": start_coordinates,
      "end": end_coordinates
  }

  response = requests.get(url, params=params)
  COORDINATES_LIST = []
  if response.status_code == 200:
      data = response.json()
      COORDINATES_LIST = data["features"][0]["geometry"]["coordinates"]
      COORDINATES_LIST = [[coord[1], coord[0]] for coord in COORDINATES_LIST]
      folium.PolyLine(COORDINATES_LIST, color='red').add_to(m)
  else:
    failed_coords.append(end_coordinates)
    print("Failed to fetch directions. Status code:", response.status_code)




o = ports[0][0]
d = ports[0][1]
eo = 23.632192216157847
ed = 58.56785345866717

ox = ports[1][0]
dx = ports[1][1]
eox = 23.632192216157847
edx = 58.56785345866717


oy = ports[2][0]
dy = ports[2][1]
eoy = 23.632192216157847
edy = 58.56785345866717



output = marnet_geograph.get_shortest_path(
    origin_node={"latitude":o,"longitude":d},
    destination_node={"latitude": eo,"longitude": ed},
     output_units='km'
)

output1 = marnet_geograph.get_shortest_path(
    origin_node={"latitude": ox,"longitude":dx },
    destination_node={"latitude":eox,"longitude": edx},
     output_units='km'
)

output2 = marnet_geograph.get_shortest_path(
    origin_node={"latitude": oy, "longitude":dy},
    destination_node={"latitude":eoy,"longitude":edy},
     output_units='km'
)



x = (([[i['latitude'],i['longitude']] for i in output['coordinate_path']]))
y = (([[i['latitude'],i['longitude']] for i in output1['coordinate_path']]))
z = (([[i['latitude'],i['longitude']] for i in output2['coordinate_path']]))

# Show the length
lengthx = int(output['length']) #=> Length:  19596.4653
lengthy = int(output1['length']) #=> Length:  19596.4653
lengthz = int(output2['length']) #=> Length:  19596.4653

print("Km",lengthx,"Time",lengthx/37)
print("Km",lengthy,"Time",lengthy/37)
print("Km",lengthz,"Time",lengthz/37)

find_shortest_route = [lengthx,lengthy,lengthz]

shortest_route = (min(find_shortest_route))
print(shortest_route)


line_colorx = "blue"
line_colory ="blue"
line_colorz = "blue"

for i in range(len(find_shortest_route)):
  if find_shortest_route[i] == shortest_route:
    if i == 0:
      print("Green x")
      line_colorx= "green"

    if i == 1:
      print("Green y")
      line_colorx= "green"
     

    if i == 2:
      print("Green z")
      line_colorx= "green"


folium.TileLayer('cartodbdark_matter').add_to(m)
folium.PolyLine(x, color=line_colorx, weight=2.5, opacity=1 ,tooltip=('KM :',lengthx)).add_to(m)
folium.PolyLine(y, color=line_colory, weight=2.5, opacity=1,tooltip=('KM',lengthy)).add_to(m)
folium.PolyLine(z, color=line_colorz, weight=2.5, opacity=1,tooltip=('KM',lengthz)).add_to(m)

m.save("map.html")

