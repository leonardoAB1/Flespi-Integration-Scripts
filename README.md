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
    "ident": "################",
    "meta": null,
    "secondary": false,
    "source": "###.##.#.###:#####",
    "transport": "tcp"
}
```

#### flespi_mqtt_api_usecase_03

- **Description:** MQTT Client Script with Flespi Integration to get Scooter's General Info.
- **MQTT Topic:** `flespi/state/gw/devices/{device_id}`
- **Sample Responses:**
- 
```json
{
    "cid": "#######",
    "configuration": {
        "ident": "################",
        "settings_polling": "once"
    },
    "device_type_id": 1272,
    "id": 5537057,
    "media_rotate": 0,
    "media_ttl": 31536000,
    "messages_rotate": 0,
    "messages_ttl": 31536000,
    "name": "SomeName",
    "protocol_id": 200
}
```

### REST API Integration Scripts

#### flespi_res_api_usecase_00.py

- **Description:** Script using Flespi REST API to retrieve data about all registered devices.
- **API Endpoint:** `https://flespi.io/mqtt/sessions/all`
- **Sample Response:**
```json
{
  "result": [
    {
      "size": 0,
      "ip": "###.###.###.##",
      "id": "##########",
      "connected": true,
      "cid": "#######",
      "clean": true,
      "client_id": "panel-4.45.24-########",
      "expires": 0
    },
    {
      "size": 0,
      "ip": "###.###.###.##",
      "id": "##########",
      "connected": true,
      "cid": "#######",
      "clean": true,
      "client_id": "apibox-0.6.11-########",
      "expires": 0
    },
    {
      "size": 0,
      "ip": "###.###.###.##",
      "id": "##########",
      "connected": true,
      "cid": "#######",
      "clean": true,
      "client_id": "helpbox-2.6.1-########",
      "expires": 0
    }
  ]
}
```

#### flespi_res_api_usecase_01.py

- **Description:** Script using Flespi REST API to get telemetry data for a specific device's altitude, latitude, and longitude.
- **API Endpoint:** `https://flespi.io/gw/devices/{device_id}/telemetry/{parameter}`
- **Sample Responses:**
```json
{
  "result": [
    {
      "id": 5537057,
      "telemetry": {
        "position.altitude": {
          "ts": 1706905852,
          "value": 412.1
        }
      }
    }
  ]
}
```

```json
{
  "result": [
    {
      "id": 5537057,
      "telemetry": {
        "position.latitude": {
          "ts": 1706905852,
          "value": -17.72436
        }
      }
    }
  ]
}
```

```json
{
  "result": [
    {
      "id": 5537057,
      "telemetry": {
        "position.longitude": {
          "ts": 1706905852,
          "value": -63.171493
        }
      }
    }
  ]
}
```

#### flespi_res_api_usecase_02.py
- **Description:** Retrieves historic data for a specified device. It prints the historic location data, including latitude, longitude, and timestamp, and visualizes the device's path by plotting points on a map using geopandas and matplotlib libraries. The script also fetches and utilizes an authorization token from environment variables for secure API access.
- **API Endpoint:** `https://flespi.io/gw/devices/{device_id}/messages`
- **Sample Responses:**
```json
{
  "result": [
    {
      "battery.level": 90,
      "battery.voltage": 4.11,
      "channel.id": 1190401,
      "device.id": 5537057,
      "device.name": "SomeName",
      "device.type.id": 1272,
      "gsm.signal.level": 65,
      "ident": "################",
      "message.type": "Q0",
      "peer": "###.##.##.###:#####",
      "protocol.id": 200,
      "server.timestamp": 1706760540.344204,
      "timestamp": 1706760540.344204,
      "vendor.code": "OM"
    },
    {
      "channel.id": 1190401,
      "device.id": 5537057,
      "device.name": "SomeName",
      "device.type.id": 1272,
      "ident": "################",
      "indication.mode": "A",
      "message.type": "D0",
      "peer": "###.##.##.###:#####",
      "position.altitude": 398.7,
      "position.hdop": 0.97,
      "position.latitude": -17.724326,
      "position.longitude": -63.171542,
      "position.satellites": 11,
      "position.valid": true,
      "protocol.id": 200,
      "server.timestamp": 1706760560.319966,
      "timestamp": 1706760559,
      "vendor.code": "OM"
    },
    {
      "battery.charging.status": false,
      "battery.level": 90,
      "battery.voltage": 4.11,
      "channel.id": 1190401,
      "device.id": 5537057,
      "device.name": "SomeName",
      "device.type.id": 1272,
      "gsm.signal.level": 65,
      "ident": "################",
      "lock.status": true,
      "message.type": "H0",
      "peer": "###.##.##.###:#####",
      "protocol.id": 200,
      "server.timestamp": 1706760600.823599,
      "timestamp": 1706760600.823599,
      "vendor.code": "OM"
    },
    ....
  ]
}
```