import geopandas as gpd
import json
from shapely.geometry import Point
import folium
with open('airports.json', encoding='utf-8') as f:
    data = json.load(f)
ports_gdf = gpd.GeoDataFrame(data)

# Step 3: Convert latitude and longitude to Point geometry
ports_gdf['geometry'] = ports_gdf.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)


def getRoutes(start_coordinates):
  your_point = gpd.GeoDataFrame({'geometry': [Point(start_coordinates.split(',')[0], start_coordinates.split(',')[1])]}, crs=ports_gdf.crs)
  nearest_port_index = ports_gdf.distance(your_point.unary_union)
  sorted = nearest_port_index.sort_values()
  indexes = sorted.iloc[:3].index
  print(indexes)


  import requests
  import folium
  import polyline
  from pyproj import CRS, Transformer
  crs_hk80 = CRS.from_proj4("+proj=tmerc +lat_0=22.31213333333334 +lon_0=114.1785555555556 +k=1 +x_0=836694.05 +y_0=819069.8 +ellps=intl +towgs84=-162.619,-276.959,-161.764,0.067753,-2.24365,-1.15883,-1.09425 +units=m +no_defs ")
  transformer = Transformer.from_crs(crs_hk80, 4326)
  transformer.transform(835000, 812000)
  INTERSECTION_ID = 'Start'
  url = "https://api.openrouteservice.org/v2/directions/driving-car/json"
  # api_key = "5b3ce3597851110001cf6248846d6a68ec334aaaa34195cdcd3f11ad"
  api_key = "5b3ce3597851110001cf6248bef52906ad594343afbb98f64d4f4fa0"
  failed_coords = []
  # end_coordinates = "72.963540, 18.952151"
  
  folium.Marker((start_coordinates.split(',')[1], start_coordinates.split(',')[0]), tooltip=folium.Tooltip(INTERSECTION_ID, permanent=True)).add_to(m)


  ports = []
  for i in indexes:
    ports.append([ports_gdf.iloc[i]["latitude"],ports_gdf.iloc[i]["longitude"]])
    print(ports_gdf.iloc[i]["latitude"],ports_gdf.iloc[i]["longitude"])
    end_coordinates = str(ports_gdf.iloc[i]["longitude"]) + "," + str(ports_gdf.iloc[i]["latitude"])
    body = {
        "coordinates": [start_coordinates.split(','), end_coordinates.split(',')],
        "radiuses": [-1]
    }
    print(body)
    headers = {
        "Authorization": api_key
    }

    response = requests.post(url, json=body, headers=headers)
    COORDINATES_LIST = []
    if response.status_code == 200:
        data = response.json()
        print(data)
        COORDINATES_LIST = data["routes"][0]["geometry"]
        decoded_coordinates = polyline.decode(COORDINATES_LIST)
        COORDINATES_LIST= []
        for lat, lon in decoded_coordinates:
          COORDINATES_LIST.append([lat, lon])
        folium.PolyLine(COORDINATES_LIST, color='red').add_to(m)
    else:
      failed_coords.append(end_coordinates)
      print("Failed to fetch directions. Status code:", response.json())
  return ports


start_coordinates="74.361627, 29.577676"
m = folium.Map(location=(start_coordinates.split(',')[1], start_coordinates.split(',')[0]))
portsfrom=getRoutes(start_coordinates)
start_coordinates="137.856003, 36.429584"
portsto= getRoutes(start_coordinates)


cruising_speed_kmh = 800  # Cruising speed of the aircraft in kilometers per hour
fuel_consumption_liters_per_hour = 300  # Fuel consumption rate of the aircraft in liters per hour
fuel_cost_per_liter = 2  # Fuel cost per liter in dollars

from math import radians, sin, cos, sqrt, atan2
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

flightinfo = []
from folium.plugins import AntPath
import np
for ii in range(3):
    coordinates = [portsfrom[ii], portsto[ii]]
    ant_path = AntPath(locations=coordinates, dash_array=[10, 20], delay=800, color='blue', pulse_color='orange')
    m.add_child(ant_path)


    distance = calculate_distance(*portsfrom[ii], *portsto[ii])

    # Calculate flight time (hours)
    flight_time_hours = distance / cruising_speed_kmh

    # Calculate fuel consumption (liters)
    fuel_consumption_liters = fuel_consumption_liters_per_hour * flight_time_hours

    # Calculate fuel cost
    fuel_cost = fuel_consumption_liters * fuel_cost_per_liter

    flightinfo.append({
       "distance": distance,
       "time": flight_time_hours,
       "fule": fuel_consumption_liters,
       "cost": fuel_cost

    })

print(flightinfo)
m.save("templates/airmap.html")