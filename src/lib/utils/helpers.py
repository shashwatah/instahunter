import requests

def request_raw_data(url, headers):
    try:
        request = requests.get(url=url, headers=headers)
        response_json = request.json()
    except:
        raise Exception("Error fetching data")

    return response_json