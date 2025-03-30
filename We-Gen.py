import folium
from folium.plugins import HeatMap
import pandas as pd
import json
import os
from google.cloud import storage

# Specify the Google Cloud Storage Bucket name
bucket_name = "your_gcp_bucket_name"  # Replace with your GCP bucket name

# Set up Google Cloud Storage Client
client = storage.Client()

# Function to download the latest CSV file from GCP bucket
def download_latest_csv(bucket_name, prefix="Night_Lights_India_"):
    bucket = client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)
    
    # Find the most recent file (sorted by updated time)
    latest_blob = max(blobs, key=lambda blob: blob.updated)
    local_file_name = latest_blob.name
    latest_blob.download_to_filename(local_file_name)
    
    print(f"Downloaded: {local_file_name}")
    return local_file_name

# Download the latest night lights CSV file
latest_file = download_latest_csv(bucket_name)

# Load the exported CSV file
df = pd.read_csv(latest_file)

# Extract latitude, longitude, and radiance intensity
data = df[['.geo', 'avg_rad']].dropna()

# Convert the GeoJSON point format into lat/lon
def extract_coords(geo_str):
    geo_json = json.loads(geo_str)
    return [geo_json['coordinates'][1], geo_json['coordinates'][0]]  # Lat, Lon

# Apply function to extract coordinates
data[['lat', 'lon']] = data['.geo'].apply(extract_coords).apply(pd.Series)

# Prepare data for HeatMap (lat, lon, intensity)
heat_data = data[['lat', 'lon', 'avg_rad']].values.tolist()

# Create a Folium map centered over India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add heat map layer
HeatMap(heat_data).add_to(m)

# Save map to an HTML file
map_file = "light_pollution_heatmap.html"
m.save(map_file)

print(f"Heat map saved as {map_file}")

# Optionally, display map (if using Jupyter Notebook or locally)
m