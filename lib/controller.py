from lib.process import process_func_dispatcher
from lib.helpers import request_raw_data

def main_controller(answers):
    raw_data = request_raw_data(answers['query_type'], answers['query'])

    if 'post_type' in answers:
        process_func_dispatcher[answers['query_type']](raw_data, answers['post_type'])
    else:
        process_func_dispatcher[answers['query_type']](raw_data)