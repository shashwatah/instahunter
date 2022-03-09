from rich.console import Console

from lib.io import display_header, get_input, create_json_file, display_data, display_message
from lib.data import request_raw_data, processor

def controller(console):
    input = get_input()

    with console.status('[bold green]Fetching Data...') as status:
        raw_data = request_raw_data(input['query_type'], input['query'])
        
        if len(raw_data) == 0:
            raise Exception("Request returned no results.")
        
        if 'post_type' in input:
            processed_data = processor[input['query_type']](raw_data, input['post_type'])
        else:   
            processed_data = processor[input['query_type']](raw_data)

    if input['file_confirm']:
        file_name = create_json_file(input['query'], processed_data)
        display_message(f'Data Fetched! [bold red]{file_name}[/bold red] created :thumbs_up:')
    else:
        display_data(processed_data)
        display_message('Done! :thumbs_up:')

if __name__  == '__main__':
    console = Console()

    display_header()

    try:
        controller(console)
    except (KeyboardInterrupt, KeyError, SystemError):
        display_message("Bye! :waving_hand:")
    except Exception as error:
        display_message(str(error), False)
