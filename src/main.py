from lib.io import display_header, get_input, display_data
from lib.processor import dispatcher
from lib.utils.helpers import request_raw_data

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

api_urls = {
    'posts': 'https://www.instagram.com/explore/tags/%s/?__a=1',
    'user_data': 'https://www.instagram.com/%s/?__a=1',
    'user_posts': 'https://www.instagram.com/%s/?__a=1',
    'search': 'https://www.instagram.com/web/search/topsearch/?query=%s'
}

def controller():
    input = get_input()

    api_url = api_urls[input['query_type']]%input['query']
    raw_data = request_raw_data(api_url, headers)

    if 'post_type' in input:
        processed_data = dispatcher[input['query_type']](raw_data, input['post_type'])
    else:
        processed_data = dispatcher[input['query_type']](raw_data)

    display_data(processed_data)


if __name__  == '__main__':
    display_header()
    controller()
