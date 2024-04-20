import folium
from scgraph.geographs.marnet import marnet_geograph
from folium.plugins import AntPath
from geopy.geocoders import Nominatim


d = 72.81618701073049
o = 19.016382787157564
eo = -33.84364770096933
ed = 151.23727447605867
sgo = 2.998225
sgd = 101.390955

def check_in_australia(latitude, longitude):
    print(latitude, longitude)
    geolocator = Nominatim(user_agent="geoapiExercises", timeout=10)
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    if "Australia" in location.address:
        return True
    else:
        return False


is_in_australia = check_in_australia(eo, ed)
print("Are the coordinates in Australia?", is_in_australia)
m = folium.Map(location=(o, d))
custom_icon_red = folium.features.CustomIcon("https://cdn.iconscout.com/icon/premium/png-512-thumb/red-ball-1922591-1630524.png", icon_size=(50, 50))
custom_icon_green = folium.features.CustomIcon("https://cdn.iconscout.com/icon/premium/png-512-thumb/green-circle-1912985-1628595.png", icon_size=(50, 50))
folium.Marker(location=[o, d], icon=custom_icon_green).add_to(m)
folium.Marker(location=[eo, ed], icon=custom_icon_red).add_to(m)


if(is_in_australia):
    custom_icon = folium.features.CustomIcon("https://cdn.iconscout.com/icon/premium/png-512-thumb/transshipment-714768.png", icon_size=(50, 50))
    folium.Marker(location=[sgo, sgd], icon=custom_icon).add_to(m)

    output = marnet_geograph.get_shortest_path(
            origin_node={"latitude":o,"longitude":d},
            destination_node={"latitude": sgo,"longitude": sgd},
            output_units='km'
        )


    print(output)
    x = (([[i[0],i[1]] for i in output['coordinate_path']]))
    ant_path = AntPath(locations=x, dash_array=[10, 20], delay=800, color='blue', pulse_color='orange')
    m.add_child(ant_path)
    output = marnet_geograph.get_shortest_path(
            origin_node={"latitude":sgo,"longitude":sgd},
            destination_node={"latitude": eo,"longitude": ed},
            output_units='km'
        )


    print(output)
    x = (([[i[0],i[1]] for i in output['coordinate_path']]))
    ant_path = AntPath(locations=x, dash_array=[10, 20], delay=800, color='blue', pulse_color='orange')
    m.add_child(ant_path)
else:
    output = marnet_geograph.get_shortest_path(
            origin_node={"latitude":o,"longitude":d},
            destination_node={"latitude": eo,"longitude": ed},
            output_units='km'
        )


    print(output)
    x = (([[i[0],i[1]] for i in output['coordinate_path']]))
    ant_path = AntPath(locations=x, dash_array=[10, 20], delay=800, color='blue', pulse_color='orange')
    m.add_child(ant_path)

m.save("templates/transhipment.html")