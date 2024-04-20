from flask import Flask, render_template, request
import requests
from scgraph.geographs.marnet import marnet_geograph
import folium
import geopandas as gpd
import json
from shapely.geometry import Point

app = Flask(__name__, static_url_path='/static')

# cost map declaration


f = open('ports.json')
data = json.load(f)
ports_gdf = gpd.GeoDataFrame(data)
ports_gdf['geometry'] = ports_gdf.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)


def geocode_location(location):
    url = f"https://lorrycare.com:5000/v1/suggest-name?input={location}"
    response = requests.get(url)
    data = response.json()
    data = data[0]

    print(data)
    print(data["description"])
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={data["description"]}&key=AIzaSyDluUHxWIlx9s8aaSHIUGp2YCynHftXcPY"
    response = requests.get(url)
    data = response.json()
    latlongs = data["results"][0]["geometry"]["location"]
    print(latlongs)
    return latlongs["lat"], latlongs["lng"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    print("User input:", user_input)

    user_input1 = request.form['user_input1']
    print("User input:", user_input1)

    user_date = request.form['user_date']
    print("User input:", user_date)


    location = user_input
    latitude, longitude = geocode_location(location)
    if latitude and longitude:
      origin = (f"{longitude},{latitude}")

      #Destination 

    location1 = user_input1
    latitude, longitude = geocode_location(location1)
    if latitude and longitude:
      destination = (f"{latitude},{longitude}")
      end_latitude =  latitude
      end_longitude = longitude


   
    start_coordinates = origin # probleam 


    print(origin)
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
    


    m = folium.Map(location=(start_coordinates.split(',')[1], start_coordinates.split(',')[0]))
    folium.Marker((start_coordinates.split(',')[1], start_coordinates.split(',')[0]), tooltip=folium.Tooltip(INTERSECTION_ID, permanent=True)).add_to(m)

    cost = folium.Map(location=(start_coordinates.split(',')[1], start_coordinates.split(',')[0]))
    folium.Marker((start_coordinates.split(',')[1], start_coordinates.split(',')[0]), tooltip=folium.Tooltip(INTERSECTION_ID, permanent=True)).add_to(cost)

    delivery = folium.Map(location=(start_coordinates.split(',')[1], start_coordinates.split(',')[0]))
    folium.Marker((start_coordinates.split(',')[1], start_coordinates.split(',')[0]), tooltip=folium.Tooltip(INTERSECTION_ID, permanent=True)).add_to(delivery)


    ports = []
    for i in indexes:
        ports.append((ports_gdf.iloc[i]["Latitude"],ports_gdf.iloc[i]["Longitude"]))
        print(ports_gdf.iloc[i]["Latitude"],ports_gdf.iloc[i]["Longitude"])
        end_coordinates = str(ports_gdf.iloc[i]["Longitude"]) + "," + str(ports_gdf.iloc[i]["Latitude"])
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


    print(ports)
    o = ports[0][0]
    d = ports[0][1]
    eo = end_latitude
    ed = end_longitude


    ox = ports[1][0]
    dx = ports[1][1]
    eox = end_latitude
    edx = end_longitude


    oy = ports[2][0]
    dy = ports[2][1]
    eoy = end_latitude
    edy = end_longitude


    #ad marker

    folium.Marker(
        location=[o,d],
        tooltip="Click me!",
        popup="Sea Port",
        icon=folium.Icon(color='black'),
    ).add_to(m)



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
    long_route = (max(find_shortest_route))
    print(shortest_route)


    line_colorx = "blue"
    line_colory ="blue"
    line_colorz = "blue"

    for i in range(len(find_shortest_route)):
     if find_shortest_route[i] == shortest_route:
        if i == 0:
         print("Green x")
         line_colorx= "green"
         folium.PolyLine(x, color="Orange", weight=2.5, opacity=1 ,tooltip=('KM :',lengthx)).add_to(cost)
         distance = lengthx

         fuel_consumption_per_km =  0.1
         fuel_price_per_ton = 500
         average_speed = 20
         co2_per_ton_fuel = 3.1



         total_fuel_cost = distance * fuel_consumption_per_km * fuel_price_per_ton
         delivery_time_hours = distance / average_speed
         total_fuel_consumption = distance * fuel_consumption_per_km
         total_co2_emissions = total_fuel_consumption * co2_per_ton_fuel


        
        if i == 1:
         print("Green y")
         line_colorx= "green"
         folium.PolyLine(y, color="Orange", weight=2.5, opacity=1 ,tooltip=('KM :',lengthx)).add_to(cost)

         distance = lengthy

         fuel_consumption_per_km =  0.1
         fuel_price_per_ton = 500
         average_speed = 20
         co2_per_ton_fuel = 3.1



         total_fuel_cost = distance * fuel_consumption_per_km * fuel_price_per_ton
         delivery_time_hours = distance / average_speed
         total_fuel_consumption = distance * fuel_consumption_per_km
         total_co2_emissions = total_fuel_consumption * co2_per_ton_fuel

        

        if i == 2:
         print("Green z")
         line_colorx= "green"
         folium.PolyLine(z, color="Orange", weight=2.5, opacity=1 ,tooltip=('KM :',lengthx)).add_to(cost)
         distance = lengthz

         fuel_consumption_per_km =  0.1
         fuel_price_per_ton = 500
         average_speed = 20
         co2_per_ton_fuel = 3.1



         total_fuel_cost = distance * fuel_consumption_per_km * fuel_price_per_ton
         delivery_time_hours = distance / average_speed
         total_fuel_consumption = distance * fuel_consumption_per_km
         total_co2_emissions = total_fuel_consumption * co2_per_ton_fuel



    # Best delivery time

    for i in range(len(find_shortest_route)):
     if find_shortest_route[i] == long_route:
        if i == 0:
         print("Green x")
         line_colorx= "green"
         folium.PolyLine(x, color="Green", weight=2.5, opacity=1 ,tooltip=('KM :',lengthx)).add_to(delivery)

         distance_x = lengthx

         fuel_consumption_per_km_x = 0.1
         fuel_price_per_ton_x = 500
         average_speed_x = 20
         co2_per_ton_fuel_x = 3.1

         total_fuel_cost_x = distance_x * fuel_consumption_per_km_x * fuel_price_per_ton_x
         delivery_time_hours_x = distance_x / average_speed_x
         total_fuel_consumption_x = distance_x * fuel_consumption_per_km_x
         total_co2_emissions_x = total_fuel_consumption_x * co2_per_ton_fuel_x


        if i == 1:
         print("Green y")
         line_colorx= "green"
         folium.PolyLine(y, color="Green", weight=2.5, opacity=1 ,tooltip=('KM :',lengthx)).add_to(delivery)

         distance_x = lengthy

         fuel_consumption_per_km_x = 0.1
         fuel_price_per_ton_x = 500
         average_speed_x = 20
         co2_per_ton_fuel_x = 3.1

         total_fuel_cost_x = distance_x * fuel_consumption_per_km_x * fuel_price_per_ton_x
         delivery_time_hours_x = distance_x / average_speed_x
         total_fuel_consumption_x = distance_x * fuel_consumption_per_km_x
         total_co2_emissions_x = total_fuel_consumption_x * co2_per_ton_fuel_x
        

        if i == 2:
         print("Green z")
         line_colorx= "green"
         folium.PolyLine(z, color="Green", weight=2.5, opacity=1 ,tooltip=('KM :',lengthx)).add_to(delivery)
         distance_x = lengthz

         fuel_consumption_per_km_x = 0.1
         fuel_price_per_ton_x = 500
         average_speed_x = 20
         co2_per_ton_fuel_x = 3.1

         total_fuel_cost_x = distance_x * fuel_consumption_per_km_x * fuel_price_per_ton_x
         delivery_time_hours_x = distance_x / average_speed_x
         total_fuel_consumption_x = distance_x * fuel_consumption_per_km_x
         total_co2_emissions_x = total_fuel_consumption_x * co2_per_ton_fuel_x


    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.PolyLine(x, color=line_colorx, weight=2.5, opacity=1 ,tooltip=('KM :',lengthx)).add_to(m)
    folium.PolyLine(y, color=line_colory, weight=2.5, opacity=1,tooltip=('KM',lengthy)).add_to(m)
    folium.PolyLine(z, color=line_colorz, weight=2.5, opacity=1,tooltip=('KM',lengthz)).add_to(m)

    #

    m.save("templates/map.html")

    folium.TileLayer('cartodbdark_matter').add_to(cost)
    cost.save("templates/cost.html")

    folium.TileLayer('cartodbdark_matter').add_to(delivery)
    delivery.save("templates/delivery.html")


    print("New Map is return")

    print("\nCost:", total_fuel_cost)
    print("Delivery Time (hours):", delivery_time_hours)
    print("Fuel Consumption (tons):", total_fuel_consumption)
    print("CO2 Emissions (tons):", total_co2_emissions)
        


    return render_template('main.html',cost=total_fuel_cost, delivery_time=delivery_time_hours, carbon= total_co2_emissions,fuel=total_fuel_consumption,  costx=total_fuel_cost_x, delivery_time_hours_x = delivery_time_hours_x,totoal_fuel_consum =total_fuel_consumption_x,carbon_x =total_co2_emissions_x)


@app.route('/weather')
def weather():
    return render_template('weather.html')  # Serve the map.html file

@app.route('/map')
def map():
    return render_template('map.html')  # Serve the map.html file

@app.route('/cost')
def cost():
    return render_template('cost.html' )  # Serve the map.html file

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')  # Serve the map.html file

@app.route('/sugggested')
def suggested():
    return render_template('suggested.html')  # Serve the map.html file



if __name__ == '__main__':
    app.run(debug=True)
