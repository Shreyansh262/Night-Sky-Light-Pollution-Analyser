import ee
from datetime import datetime, timedelta

# Initialize Earth Engine API
ee.Initialize()

# Define region of interest (India)
region = ee.Geometry.Rectangle([68, 6, 97, 37])  # Approximate India bounds

# Get today's date
today = datetime.now()

# Get yesterday's date for exporting the previous day's data
yesterday = today - timedelta(days=1)
start_date = yesterday.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

# Load VIIRS night-time light dataset for yesterday's date
dataset = ee.ImageCollection("NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG") \
            .filterDate(start_date, end_date) \
            .median() \
            .select('avg_rad')  # Select average radiance band

# Sample points within the region
sampled_points = dataset.sample(
    region=region,
    scale=10000,   # 10km resolution
    numPixels=500, # Number of sample points
    geometries=True
)

# Export data as CSV to Google Cloud Storage
task = ee.batch.Export.table.toCloudStorage(
    collection=sampled_points,
    description=f"Night_Lights_India_{start_date}",
    bucket="your_gcp_bucket_name",  # Replace with your GCP bucket name
    fileNamePrefix=f"Night_Lights_India_{start_date}",
    fileFormat="CSV"
)
task.start()

print(f"Export task started for date: {start_date}")