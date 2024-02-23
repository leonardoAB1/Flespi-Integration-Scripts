import os
import requests
import json
import time

flespi_ids = [5543996, 5542298, 5542304, 5542306, 5542307, 5542309, 5542310, 
              5542311, 5543991, 5539228, 5543997, 5543999, 5544000, 5544004, 
              5544005, 5544006, 5544007, 5544008, 5544011, 5544013, 5544014, 
              5544017, 5544018, 5544022, 5544025, 5544026, 5544031, 5544032, 
              5544033, 5544035, 5544037, 5544038, 5544041, 5544043, 5544045, 
              5544047, 5544048, 5544049, 5544050, 5544051, 5544052, 5542312, 
              5544053, 5544054, 5544055, 5544056, 5544058, 5544059, 5544063, 5544064]

for id in flespi_ids:
    url = f'https://flespi.io/gw/devices/{id}?fields=messages_ttl'
    headers = {
        'Authorization': f'FlespiToken {os.environ.get("FlespiToken")}',
        'Content-Type': 'application/json'
    }
    data = {
        'messages_ttl': 1
    }

    response = requests.patch(url, headers=headers, json=data)
    print(response)
    
time.sleep(60*4)

for id in flespi_ids:
    url = f'https://flespi.io/gw/devices/{id}?fields=messages_ttl'
    headers = {
        'Authorization': f'FlespiToken {os.environ.get("FlespiToken")}',
        'Content-Type': 'application/json'
    }
    data = {
        'messages_ttl': 2592000
    }

    response = requests.patch(url, headers=headers, json=data)
    print(response)

    