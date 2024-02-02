# Flespi Integration Scripts

This repository houses a set of Python scripts designed for integration with the Flespi platform, employing both MQTT and REST APIs. The scripts serve as illustrative examples for diverse use cases, including but not limited to real-time message retrieval, scooter location tracking, active TCP connection monitoring from a device, and retrieving details about registered devices.

For comprehensive documentation, please refer to the [General Documentation](https://flespi.io/docs/#/mqtt/sessions).  
Additionally, you can find information about tokens and access keys in the [Token Documentation](https://flespi.com/kb/tokens-access-keys-to-flespi-platform#token-groups).


## Jan Bartnitsky. Integration with flespi: REST API, streams, MQTT

[![Watch the video](https://img.youtube.com/vi/nB2NVsyEfok/maxresdefault.jpg)](https://www.youtube.com/watch?v=nB2NVsyEfok)


## Scripts Overview

### MQTT Integration Scripts
**Documentation:** [Flespi MQTT Topics](https://flespi.com/kb/mqtt-topics)

#### flespi_mqtt_api_usecase_00.py

- **Description:** MQTT client script for real-time message retrieval from a specific device.
- **MQTT Topic:** `flespi/message/gw/devices/{device_id}`
- **Sample Response:**
```json
{
  "battery.charging.status":false,
  "battery.level":70,
  "battery.voltage":4.09,
  "channel.id":1190401,
  "device.id":5539228,
  "device.name":"scooterMobi010",
  "device.type.id":1272,
  "gsm.signal.level":90,
  "ident":"015136001986400",
  "lock.status":true,
  "message.type":"H0",
  "peer": "###.##.#.###:#####",
  "protocol.id":200,
  "server.timestamp":1706905170.17258,
  "timestamp":1706905170.17258,
  "vendor.code":"OM" 
}
```

#### flespi_mqtt_api_usecase_01.py

- **Description:** MQTT client script to get the scooter's real-time location.
- **MQTT Topic:** `flespi/state/gw/devices/{device_id}/telemetry/position`
- **Sample Response:**
```json
{
    "altitude": 408.9,
    "hdop": 0.87,
    "latitude": -17.72436,
    "longitude": -63.171508,
    "satellites": 9,
    "valid": true
}
```

#### flespi_mqtt_api_usecase_02.py

- **Description:** MQTT client script to retrieve a list of active TCP connections from a device.
- **MQTT Topic:** `flespi/state/gw/devices/{device_id}/connections/+`
- **Sample Response:**
```json
{
    "channel_id": 1190401,
    "device_id": 5537057,
    "established": 1706877098.857462,
    "id": 3492206331502027,
    "ident": "015136001973812",
    "meta": null,
    "secondary": false,
    "source": "###.##.#.###:#####",
    "transport": "tcp"
}
```

### REST API Integration Scripts

#### flespi_res_api_usecase_00.py

- **Description:** Script using Flespi REST API to retrieve data about all registered devices.
- **API Endpoint:** `https://flespi.io/mqtt/sessions/all`

#### flespi_res_api_usecase_01.py

- **Description:** Script using Flespi REST API to get telemetry data for a specific device's altitude, latitude, and longitude.
- **API Endpoint:** `https://flespi.io/gw/devices/{device_id}/telemetry/{parameter}`
