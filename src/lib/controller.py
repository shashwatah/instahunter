from lib.view.view import get_input, display_data
from lib.process import process_func_dispatcher
from lib.helpers import request_raw_data

def controller():
    input = get_input()

    raw_data = request_raw_data(input['query_type'], input['query'])

    if 'post_type' in input:
        processed_data = process_func_dispatcher[input['query_type']](raw_data, input['post_type'])
    else:
        processed_data = process_func_dispatcher[input['query_type']](raw_data)

    display_data(processed_data)