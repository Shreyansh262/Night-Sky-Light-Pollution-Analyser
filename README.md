# Night-Sky-Light-Pollution-Analyser
Code 1: Automating Night-Time Lights Data Export

This code automates the process of exporting night-time light data for India using the NOAA/VIIRS DNB (Day/Night Band) dataset in Google Earth Engine (GEE) and saves the results as CSV files to a Google Cloud Storage (GCS) bucket. Here's what happens:

Load Dataset:

It retrieves the VIIRS night-time light data for a defined date range (in this case, daily data for the past decade).

Set Region of Interest (ROI):

The region of interest is specified as India's geographical bounds (latitude and longitude rectangle).

Sampling Points:

It samples random points from within the defined region, extracting radiance values (intensity of night-time lights) at these points.

Export Process:

Instead of saving manually, the code automates the export of the daily data to a GCS bucket. Each file is named uniquely based on the date (e.g., Night_Lights_India_YYYY-MM-DD.csv).

Automation & Scalability:

The updated version dynamically handles data exports for every date (without user intervention) and ensures the files are ready for downstream processing.


Code 2: Generating a Heat Map of Light Pollution
This second code uses Python and the Folium library to create a heat map visualizing the night-time light intensity data exported by Code 1. Here's what happens:

1. Fetch Latest CSV:

The script automatically connects to the GCS bucket where the CSV files are stored. It retrieves the most recent file, assuming it contains the latest night-time light data.

2. Read Data:

It reads the CSV file and extracts relevant fields, specifically:

.geo: This contains the geographical coordinates (in GeoJSON format).

avg_rad: This field contains the night-time light radiance values.

3. Coordinate Conversion:

The GeoJSON .geo field is parsed to extract latitude and longitude coordinates for each sampled point.

4. Heat Map Creation:

Using Folium, the script generates a heat map centered over India, with higher radiance values displayed as more intense regions on the map.
