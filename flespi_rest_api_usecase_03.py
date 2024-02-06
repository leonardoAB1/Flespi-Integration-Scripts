'''
Author: Leonardo Acha Boiano
Date: 2024-02-02
Script Name: flespi_rest_api_usecase_03.py

Script with Flespi Integration to unlock and lock device thru MQTT
Retrieves lock status by MQTT
'''

import requests
import json
import time
import os

import asyncio
import signal
from gmqtt import Client as MQTTClient

device_id=5544049
url = f'https://flespi.io/gw/devices/{device_id}/commands'
headers = {
    'Authorization': f'FlespiToken {os.environ.get("FlespiToken")}',
    'Content-Type': 'application/json'
}
topic=f"flespi/state/gw/devices/{device_id}/telemetry/lock.status"
state=1 #1 to lock, 0 to unlock

# Define the data payload template
data_template = {
    "name": "setting.r0.set",
    "properties": {
        "key_time": 1,
        "lock": state,  # Will be changed dynamically
        "user_id": ""
    },
    "timeout": 10
}

# Event to signal the termination of the script
STOP = asyncio.Event()

# Callback function to handle connection to the MQTT broker
def on_connect(client, flags, rc, properties):
    client.subscribe(topic, qos=1)

# Signal handler to set the STOP event and initiate script termination
def ask_exit(*args):
    STOP.set()

# Callback function to handle incoming MQTT messages
def on_message(client, topic, payload, qos, properties):
    decoded_payload = payload.decode('utf8')
    formatted_payload = json.dumps(json.loads(decoded_payload), indent=4)

    print(f'received message in topic "{topic}":\n{formatted_payload}')
    print('disconnecting...')
    ask_exit()

# Callback function to handle disconnection from the MQTT broker
def on_disconnect(client, packet, exc=None):
    print('disconnected')

# Callback function to handle subscription success
def on_subscribe(client, mid, qos, properties):
    # Placeholder function, not used in the script
    pass

# Main asynchronous function
async def main():
    # Create an instance of the MQTTClient
    client = MQTTClient('flespi-examples-mqtt-client-python', clean_session=True)

    # Set callback functions for various events
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    # Set authentication credentials using FlespiToken from environment variables
    client.set_auth_credentials(f'FlespiToken {os.environ.get("FlespiToken")}', None)
    
    print('mqtt client created, connecting...')
    
    # Connect to the MQTT broker at mqtt.flespi.io over SSL
    await client.connect('mqtt.flespi.io', port=8883, ssl=True)
    
    # Wait for the STOP event to be set, indicating script termination
    await STOP.wait()
    
    # Disconnect from the MQTT broker
    await client.disconnect()


if __name__ == '__main__':
    # Convert the data to JSON string
    data = json.dumps([data_template])

    # Measure the time before sending the POST request
    start_time = time.time()
    
    # Send the POST request
    response = requests.post(url, headers=headers, data=data)

    # Measure the time after receiving the response
    end_time = time.time()
    
    # Print the response
    print(response.text)

    # Calculate and print the time taken
    print(f"Time taken POST request: {end_time - start_time} seconds")   

    ##################################################################

    # Measure the time before sending the POST request
    start_time = time.time()

    # Get the event loop
    loop = asyncio.get_event_loop()

    # Run the main asynchronous function until it completes
    loop.run_until_complete(main())

    # Measure the time after receiving the response
    end_time = time.time()

    print(f"Time taken MQTT subscription: {end_time - start_time} seconds")   
