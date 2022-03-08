from rich.console import Console

from lib.io import display_header, get_input, create_json_file, display_data, display_message
from lib.processor import dispatcher
from lib.utils.helpers import request_raw_data

HEADERS = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

API_URLS = {
    'posts': 'https://www.instagram.com/explore/tags/%s/?__a=1',
    'user_data': 'https://www.instagram.com/%s/?__a=1',
    'user_posts': 'https://www.instagram.com/%s/?__a=1',
    'search': 'https://www.instagram.com/web/search/topsearch/?query=%s'
}

def controller(console):
    input = get_input()

    with console.status('[bold green]Fetching Data...') as status:
        api_url = API_URLS[input['query_type']]%input['query']
        raw_data = request_raw_data(api_url, HEADERS)

        if 'post_type' in input:
            processed_data = dispatcher[input['query_type']](raw_data, input['post_type'])
        else:
            processed_data = dispatcher[input['query_type']](raw_data)

    if input['file_confirm']:
        file_name = create_json_file(input['query'], processed_data)
        display_message(f'\nFile created, File Name: [bold red]{file_name}')
    else:
        display_data(processed_data)
        display_message('\nDone! :thumbs_up:')

if __name__  == '__main__':
    console = Console()

    display_header()
    controller(console)
