from dataclasses import field
import requests

def request_raw_data(url, headers):
    print("raw data func")
    request = requests.get(url=url, headers=headers)
    return request.json()

def handle_error():
    pass
