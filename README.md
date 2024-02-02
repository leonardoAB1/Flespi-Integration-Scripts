# Flespi Integration Scripts

This repository houses a set of Python scripts designed for integration with the Flespi platform, employing both MQTT and REST APIs. The scripts serve as illustrative examples for diverse use cases, including but not limited to real-time message retrieval, scooter location tracking, active TCP connection monitoring from a device, and retrieving details about registered devices.

For comprehensive documentation, please refer to the [General Documentation](https://flespi.io/docs/#/mqtt/sessions).  
Additionally, you can find information about tokens and access keys in the [Token Documentation](https://flespi.com/kb/tokens-access-keys-to-flespi-platform#token-groups).

## Scripts Overview

### MQTT Integration Scripts
**Documentation:** [Flespi MQTT Topics](https://flespi.com/kb/mqtt-topics)

#### flespi_mqtt_api_usecase_00.py

- **Description:** MQTT client script for real-time message retrieval from a specific device.
- **MQTT Topic:** `flespi/message/gw/devices/{device_id}`

#### flespi_mqtt_api_usecase_01.py

- **Description:** MQTT client script to get the scooter's real-time location.
- **MQTT Topic:** `flespi/state/gw/devices/{device_id}/telemetry/position`

#### flespi_mqtt_api_usecase_02.py

- **Description:** MQTT client script to retrieve a list of active TCP connections from a device.
- **MQTT Topic:** `flespi/state/gw/devices/{device_id}/connections/+`

### REST API Integration Scripts

#### flespi_res_api_usecase_00.py

- **Description:** Script using Flespi REST API to retrieve data about all registered devices.
- **API Endpoint:** `https://flespi.io/mqtt/sessions/all`

#### flespi_res_api_usecase_01.py

- **Description:** Script using Flespi REST API to get telemetry data for a specific device's altitude, latitude, and longitude.
- **API Endpoint:** `https://flespi.io/gw/devices/{device_id}/telemetry/{parameter}`
