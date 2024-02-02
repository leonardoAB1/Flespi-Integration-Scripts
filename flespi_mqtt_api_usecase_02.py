'''
Author: Leonardo Acha Boiano
Date: 2024-02-02
Script Name: flespi_mqtt_api_usecase_02.py

MQTT Client Script with Flespi List of active TCP connections from device
MQTT Documentation in https://flespi.com/kb/mqtt-topics
'''


# Import necessary libraries
import os
import asyncio
import signal

# Import the MQTT client library
from gmqtt import Client as MQTTClient
device_id = 5537057

# Event to signal the termination of the script
STOP = asyncio.Event()

# Callback function to handle connection to the MQTT broker
def on_connect(client, flags, rc, properties):
    print(f'connected, subscribing to "flespi/state/gw/devices/{device_id}/connections/+" topic...')
    client.subscribe(f'flespi/state/gw/devices/{device_id}/connections/+', qos=1)

# Signal handler to set the STOP event and initiate script termination
def ask_exit(*args):
    STOP.set()

# Callback function to handle incoming MQTT messages
def on_message(client, topic, payload, qos, properties):
    print('received message in topic \n"{}": "{}"'.format(topic, payload.decode('utf8')))
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

# Sample output
# "flespi/state/gw/devices/5537057/connections/3492206331502027": "{"channel_id":1190401,"device_id":5537057,
# "established":1706877098.857462,"id":3492206331502027,
# "ident":"015136001973812","meta":null,
# "secondary":false,"source":"161.56.9.141:31431","transport":"tcp"}"