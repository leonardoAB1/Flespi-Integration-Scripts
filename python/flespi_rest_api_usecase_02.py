'''
Author: Leonardo Acha Boiano
Date: 2024-02-05
Script Name: flespi_res_api_usecase_02.py

Script with Flespi Integration to get registered devices historic data
Prints Historic location data and plots points of given device
'''

# Script to get all registered devices using the Flespi REST API

# Import necessary libraries
import requests
import os
import json
import datetime

#Plot geodata
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import csv

# Define the file name for saving CSV
csv_file = "device_locations.csv"

# Define the Flespi API endpoint URL to get all registered devices
device_id = 5544049 
reqUrl = f"https://flespi.io/gw/devices/{device_id}/messages"

# Set the authorization token from environment variables
headersList = {
    "Authorization": os.environ.get("FlespiToken")
}

# Empty payload as we are making a GET request
payload = ""

# Make a GET request to the Flespi API to get all registered devices
response = json.loads(requests.request("GET", reqUrl, data=payload, headers=headersList).text)

print(json.dumps(response, indent=4))

###############################################################################################################
###############################################################################################################
###############################################################################################################

# Create an empty list to store Point objects
geometry = []

# Extract latitude, longitude, and timestamp from the API response
for entry in response['result']:
    if 'position.latitude' in entry and 'position.longitude' in entry and 'timestamp' in entry:
        latitude = float(entry['position.latitude'])
        longitude = float(entry['position.longitude'])
        timestamp = datetime.datetime.utcfromtimestamp(entry['timestamp'])
        timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')

        # Print the details
        print(f"Latitude: {latitude}, Longitude: {longitude}, Timestamp: {timestamp_str}")

        # Create a Point object and append to the list
        geometry.append(Point(longitude, latitude))

# Create a GeoDataFrame from the list of Point objects
gdf = gpd.GeoDataFrame(geometry=geometry, crs="EPSG:4326")

# Plot the GeoDataFrame
ax = gdf.plot(marker='o', color='red', markersize=10)
ax.set_title('Device Locations')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Open the CSV file in write mode
with open(csv_file, mode='w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["lat", "lng"])
    
    # Write data to the CSV file
    for entry in response['result']:
        if 'position.latitude' in entry and 'position.longitude' in entry and 'timestamp' in entry:
            latitude = float(entry['position.latitude'])
            longitude = float(entry['position.longitude'])
            
            # Write the data row
            writer.writerow([latitude, longitude])

print(f"Data saved to {csv_file} successfully!")

# Show the plot
plt.show()