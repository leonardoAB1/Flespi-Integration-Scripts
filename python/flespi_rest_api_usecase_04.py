'''
Author: Leonardo Acha Boiano
Date: 2024-02-07
Script Name: flespi_rest_api_usecase_04.py

Script with Flespi REST Platform API Integration to crete new tokens
'''
import requests
import os

url = 'https://flespi.io/platform/tokens?fields='
headers = {
    'Authorization': f'FlespiToken {os.environ.get("FlespiMasterToken")}',
}
data = [{"info": "Master","access":{"type":1},"ttl":60}] 
# Name, Privileges(0=Standart, 1=Master), Time to live in seconds

response = requests.post(url, headers=headers, json=data)

print(response.text)
