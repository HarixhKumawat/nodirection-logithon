from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # Create a map centered around a specific location
    m= folium.Map(location=[51.5074, -0.1278], zoom_start=10)
    folium.TileLayer('cartodbdark_matter').add_to(m)

    # Add a marker to the map
    folium.Marker([51.5074, -0.1278], popup='London').add_to(m)

    # Render the map in the HTML template
    map_html = m._repr_html_()

    return render_template('index.html', map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
