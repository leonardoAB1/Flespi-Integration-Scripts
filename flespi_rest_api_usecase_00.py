'''
Author: Leonardo Acha Boiano
Date: 2024-02-02
Script Name: flespi_res_api_usecase_00.py

Script with Flespi Integration to get registered devices data
'''

# Script to get all registered devices using the Flespi REST API

# Import necessary libraries
import requests
import os

# Define the Flespi API endpoint URL to get all registered devices
reqUrl = "https://flespi.io/mqtt/sessions/all"

# Set the authorization token from environment variables
headersList = {
    "Authorization": os.environ.get("FlespiToken")
}

# Empty payload as we are making a GET request
payload = ""

# Make a GET request to the Flespi API to get all registered devices
response = requests.request("GET", reqUrl, data=payload, headers=headersList)

# Print the response text (which contains information about all registered devices)
print(response.text)