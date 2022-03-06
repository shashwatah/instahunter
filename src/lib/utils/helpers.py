import requests

def request_raw_data(url, headers):
    print("raw data func")
    request = requests.get(url=url, headers=headers)
    return request.json()

def create_json_file():
    pass

def handle_error():
    pass
