'''
Author: Leonardo Acha Boiano
Date: 2024-02-02
Script Name: flespi_res_api_usecase_01.py

Script with Flespi Integration to get registered devices location
'''

# Import necessary libraries
import requests
import os

# Define the telemetry data fields to retrieve
data = ["position.altitude", "position.latitude", "position.longitude"]

# Specify the device id
device_id = 5537057

# Set the authorization token from environment variables
headersList = {
    "Authorization": os.environ.get("FlespiToken")
}

# Empty payload as we are making a GET request
payload = ""

# Loop through each telemetry data field and make a GET request to the Flespi API
for i in data:
    # Construct the API endpoint URL for the specific telemetry data field
    endpoint_url = f"https://flespi.io/gw/devices/{device_id}/telemetry/{i}"
    
    # Make the GET request and print the response text
    print(requests.request("GET", endpoint_url, data=payload, headers=headersList).text)

# Sample output:
# {"result":[{"id":5537057,"telemetry":{"position.altitude":{"ts":1706890490,"value":396.9}}}]}
# {"result":[{"id":5537057,"telemetry":{"position.latitude":{"ts":1706890490,"value":-17.724375}}}]}
# {"result":[{"id":5537057,"telemetry":{"position.longitude":{"ts":1706890490,"value":-63.171496}}}]}
