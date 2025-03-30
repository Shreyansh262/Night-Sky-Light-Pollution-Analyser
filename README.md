# Night-Sky-Light-Pollution-Analyser
Resources:
# Automated Night-Time Light Data Export and Visualization

## Overview
This project automates the extraction, storage, and visualization of night-time light intensity data for India using Google Earth Engine (GEE) and Google Cloud Platform (GCP). The workflow consists of two key parts:
1. *Data Export*: Automating the daily export of night-time light radiance data to Google Cloud Storage.
2. *Heat Map Visualization*: Creating a heat map of light pollution based on the exported data.

---

## Workflow
### 1. Data Export
- The Python script retrieves data from the VIIRS night-time light dataset for India.
- Sampling points are extracted to measure average radiance values.
- Daily data is exported as CSV files to a specified GCP bucket for automated processing.

### 2. Heat Map Creation
- The most recent CSV file is fetched automatically from the GCP bucket.
- Latitude, longitude, and radiance intensity values are extracted from the file.
- A heat map of light pollution over India is generated using Folium and saved as an interactive HTML file.

---
Links:
VIIRS Night-Time Light Dataset Description:
https://developers.google.com/earth-engine/datasets/catalog/NOAA_VIIRS_DNB_MONTHLY_V1_VCMSLCFG 
https://developers.google.com/earth-engine
https://cloud.google.com/storage/docs
https://cloud.google.com/scheduler/docs
https://cloud.google.com/pubsub/docs
https://python-visualization.github.io/folium/latest/
https://pandas.pydata.org/

### Google Earth Engine Python API Documentation:

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
