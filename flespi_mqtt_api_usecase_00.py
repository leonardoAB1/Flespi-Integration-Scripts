'''
Author: Leonardo Acha Boiano
Date: 2024-02-02
Script Name: flespi_mqtt_api_usecase_00.py

MQTT Client Script with Flespi Integration to
get new messages from the device in real-time
MQTT Documentation in https://flespi.com/kb/mqtt-topics
'''

# Import necessary libraries
import os
import asyncio
import signal
import json

# Import the MQTT client library
from gmqtt import Client as MQTTClient

# Specify the device id
device_id = 5539228

# Event to signal the termination of the script
STOP = asyncio.Event()

# Callback function to handle connection to the MQTT broker
def on_connect(client, flags, rc, properties):
    print(f'connected, subscribing to "flespi/message/gw/devices/{device_id}" topic...')
    client.subscribe(f'flespi/message/gw/devices/{device_id}', qos=1)

# Signal handler to set the STOP event and initiate script termination
def ask_exit(*args):
    STOP.set()

# Callback function to handle incoming MQTT messages
def on_message(client, topic, payload, qos, properties):
    decoded_payload = payload.decode('utf8')
    formatted_payload = json.dumps(json.loads(decoded_payload), indent=4)

    print('received message in topic "{}":\n{}'.format(topic, formatted_payload))
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
    client.set_auth_credentials('FlespiToken {}'.format(os.environ.get("FlespiToken")), None)
    
    print('mqtt client created, connecting...')
    
    # Connect to the MQTT broker at mqtt.flespi.io over SSL
    await client.connect('mqtt.flespi.io', port=8883, ssl=True)
    
    # Wait for the STOP event to be set, indicating script termination
    await STOP.wait()
    
    # Disconnect from the MQTT broker
    await client.disconnect()


# Entry point of the script
if __name__ == '__main__':
    # Get the event loop
    loop = asyncio.get_event_loop()

    # Run the main asynchronous function until it completes
    loop.run_until_complete(main())
