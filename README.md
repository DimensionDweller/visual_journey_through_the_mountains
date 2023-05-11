# Visual Journey Through The Mountains using Apple Health Data

This project visualizes your hiking journey using the route data exported from Apple Health and photos taken along the way. The final output is an interactive map with your route, altitude changes color-coded, and photos placed on their respective geolocations.

## Table of Contents

Project Structure
Prerequisites
Installation
Usage
Contributing
License

Project Structure <a name="project-structure"></a>

The project has the following key files:

main.py: The main driver script that manages data processing, map creation, and saving the final output. It uses the functions defined in get_workout_routes.py to process Apple Health .gpx files and uses folium library to create an interactive map.
get_workout_routes.py: This script contains a collection of functions that process workout route data from Apple Health's exported .gpx files. Functions include parse_gpx, which extracts latitude, longitude, and elevation data, and add_polyline_to_map, which adds color-coded altitude data to the folium map.
requirements.txt: This file lists the Python dependencies required to run this project. It includes packages like gpxpy for parsing .gpx files, PIL and exifread for processing images, and folium for generating interactive maps.
Prerequisites <a name="prerequisites"></a>

Before running this project, ensure you have the following:

Exported workout data from Apple Health in .gpx format.
Saved the workout route .gpx files to the workout-routes folder.
Saved your geotagged photos from your hikes to the photos folder.
Installation <a name="installation"></a>

Follow these steps to set up the project:

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/visual_journey_through_the_mountains.git
Navigate into the project directory:
bash
Copy code
cd visual_journey_through_the_mountains
Set up a Python virtual environment (optional but recommended):
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the required Python dependencies:
bash
Copy code
pip install -r requirements.txt
Usage <a name="usage"></a>

To run this project:

Update the main.py script with your desired start and end dates, photo directory, and output map file name.
Execute the main script:
bash
Copy code
python main.py
Open the generated .html file in your web browser to visualize your journey!
Contributing <a name="contributing"></a>

Contributions are welcome! If you encounter any problems or have suggestions for improvements, please open an issue.

License <a name="license"></a>

This project is licensed under the terms of the MIT license.

