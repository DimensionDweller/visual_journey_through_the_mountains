# Visual Journey Through The Mountains using Apple Health Data

This project visualizes your hiking journey using the route data exported from Apple Health and photos taken along the way. The final output is an interactive map with your route, altitude changes color-coded, and photos placed on their respective geolocations.

## Check it out here:
![link](https://645d6ec1cbb79215784d693d--enchanting-palmier-8f33ef.netlify.app)

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Project Structure <a name="project-structure"></a>

The project has the following key files:

- `main.py`: The main driver script that manages data processing, map creation, and saving the final output. It uses the functions defined in `get_workout_routes.py` to process Apple Health `.gpx` files and uses `folium` library to create an interactive map.

- `get_workout_routes.py`: This script contains a collection of functions that process workout route data from Apple Health's exported `.gpx` files. Functions include `parse_gpx`, which extracts latitude, longitude, and elevation data, and `add_polyline_to_map`, which adds color-coded altitude data to the `folium` map.

- `requirements.txt`: This file lists the Python dependencies required to run this project. It includes packages like `gpxpy` for parsing `.gpx` files, `PIL` and `exifread` for processing images, and `folium` for generating interactive maps.

## Prerequisites <a name="prerequisites"></a>

Before running this project, ensure you have the following:

1. Exported workout data from Apple Health in `.gpx` format.
2. Saved the workout route `.gpx` files to the `workout-routes` folder.
3. Saved your geotagged photos from your hikes to the `photos` folder.

## Installation <a name="installation"></a>

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/visual_journey_through_the_mountains.git
   ```

2. Navigate into the project directory:
   ```bash
   cd visual_journey_through_the_mountains
   ```

3. Set up a Python virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage <a name="usage"></a>

To run this project:

1. Update the `main.py` script with your desired start and end dates, photo directory, and output map file name.

2. Execute the main script:
   ```bash
   python main.py
   ```

3. Open the generated `.html` file in your web browser to visualize your journey!

## Contributing <a name="contributing"></a>

Contributions are welcome! If you encounter any problems or have suggestions for improvements, please open an issue.

## License <a name="license"></a>

This project is licensed under the terms of the MIT license.

