import requests

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

api_urls = {
    'posts': 'https://www.instagram.com/explore/tags/%s/?__a=1',
    'user_data': 'https://www.instagram.com/%s/?__a=1',
    'user_posts': 'https://www.instagram.com/%s/?__a=1',
    'search': 'https://www.instagram.com/web/search/topsearch/?query=%s'
}

def request_raw_data(query_type, query):
    print("raw data func")
    request = requests.get(url=api_urls[query_type]%query, headers=headers)
    return request.json()