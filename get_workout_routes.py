import gpxpy
import os
from lxml import etree
from datetime import datetime
import json
import pandas as pd
import pytz
import folium
from folium import Marker, Icon
from PIL import Image
from GPSPhoto import gpsphoto
from folium import IFrame
import exifread
from base64 import b64encode
import io
import base64
import numpy as np

def extract_gpx_data_in_date_range(directory, start_date, end_date):
    gpx_data = []

    for file in os.listdir(directory):
        if file.endswith(".gpx"):
            file_path = os.path.join(directory, file)
            try:
                with open(file_path, 'r') as gpx_file:
                    gpx = gpxpy.parse(gpx_file)
                    for track in gpx.tracks:
                        for segment in track.segments:
                            for point in segment.points:
                                point_date = point.time.replace(tzinfo=pytz.UTC)
                                if start_date <= point_date < end_date:
                                    data_point = {
                                        'latitude': point.latitude,
                                        'longitude': point.longitude,
                                        'elevation': point.elevation,
                                        'time': point_date
                                    }
                                    gpx_data.append(data_point)
            except IOError:
                print(f"Could not read file: {file_path}")
            except Exception as e:
                print(f"Unexpected error: {e}")
    return gpx_data




def create_map(latitudes, longitudes):
    m = folium.Map(location=[latitudes.mean(), longitudes.mean()], zoom_start=10, tiles='https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png', attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap')
    return m

def add_polyline_to_map(m, positions):
        # Add the hiking route as a polyline with elevation encoded in color
    positions = list(zip(latitudes, longitudes, elevations))

    # Determine elevation ranges for color coding
    elevation_ranges = np.linspace(elevations.min(), elevations.max(), 5)  # 5 is the number of ranges you want to create

    # Create color map (replace with your preferred colors)
    colors = ['green', 'yellow', 'orange', 'red']

    for i in range(len(elevation_ranges) - 1):
        segment = []
        for j in range(len(positions) - 1):
            lat, lon, elev = positions[j]
            next_lat, next_lon, next_elev = positions[j + 1]
            if elev >= elevation_ranges[i] and elev < elevation_ranges[i + 1] and next_elev >= elevation_ranges[i] and next_elev < elevation_ranges[i + 1]:
                segment.append((lat, lon))
            else:
                if len(segment) > 0:
                    folium.PolyLine(segment, color=colors[i], weight=2.5, opacity=1).add_to(m)
                    segment = []
        if len(segment) > 0:
            folium.PolyLine(segment, color=colors[i], weight=2.5, opacity=1).add_to(m)


def add_markers_to_map(m, positions):
    latitudes, longitudes, elevations = zip(*positions)

    start_marker = Marker(
        location=[latitudes[0], longitudes[0]],
        icon=Icon(color='green'),
        popup='Start'
    )
    start_marker.add_to(m)

    max_elevation_idx = np.argmax(elevations)
    max_elevation_marker = Marker(
        location=[latitudes[max_elevation_idx], longitudes[max_elevation_idx]],
        icon=Icon(color='red'),
        popup=f'Max Elevation: {elevations[max_elevation_idx]}'
    )
    max_elevation_marker.add_to(m)

def add_photos_to_map(m, photo_dir):
    # Get a list of all jpeg files in the directory
    photo_files = [os.path.join(photo_dir, file) for file in os.listdir(photo_dir) if file.endswith('.jpeg')]
    for photo_file in photo_files:
        # Extract the geographic metadata from the photo
        data = gpsphoto.getGPSData(photo_file)
        lat = data['Latitude']
        lon = data['Longitude']

        # Open and convert image to base64
        b = io.BytesIO()
        im = Image.open(photo_file)
        im.thumbnail((80, 80))  # Adjust as needed
        im.save(b, format='PNG')
        b64 = base64.b64encode(b.getvalue())

        # Create a marker at the photo's coordinates with the photo in its popup
        folium.Marker(location=[lat, lon], 
                      popup=f'<img src="data:image/png;base64,{ b64.decode("utf-8") }">', 
                      icon=folium.Icon(icon="cloud")).add_to(m)

def main(start_date, end_date, photo_dir, map_file):
    gpx_directory = '/Volumes/External_Samsung_T7/Data Science/apple_health_export_5_23/workout-routes/'
    gpx_data = extract_gpx_data_in_date_range(gpx_directory, start_date, end_date)
    workouts_df = pd.DataFrame(gpx_data)

    date_filtered_workouts = workouts_df[(workouts_df['time'] >= start_date) & (workouts_df['time'] < end_date)]
    positions = list(zip(date_filtered_workouts['latitude'].values, date_filtered_workouts['longitude'].values, date_filtered_workouts['elevation'].values))

    m = create_map(*zip(*positions))
    add_polyline_to_map(m, positions)
    add_markers_to_map(m, positions)

    photo_files = [os.path.join(photo_dir, file) for file in os.listdir(photo_dir) if file.endswith('.jpeg')]
    add_photos_to_map(m, photo_files)

    m.save(map_file)

if __name__ == "__main__":
    main(
        start_date=datetime(2022, 8, 1, tzinfo=pytz.UTC),
        end_date=datetime(2022, 8, 5, tzinfo=pytz.UTC),
        photo_dir='/Volumes/External_Samsung_T7/Data Science/apple_health_export_5_23/Mt Rainer Photos/',
        map_file='mt_rainer_map.html'
    )

    main(
        start_date=datetime(2022, 8, 8, tzinfo=pytz.UTC),
        end_date=datetime(2022, 8, 12, tzinfo=pytz.UTC),
        photo_dir='/Volumes/External_Samsung_T7/Data Science/apple_health_export_5_23/Copper Ridge Photos/',
        map_file='copper_ridge_map.html')




