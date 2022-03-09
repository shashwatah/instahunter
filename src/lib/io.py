from rich import print, print_json
import pyfiglet
from PyInquirer import prompt
import json

from lib.utils.question import QUESTIONS, pi_custom_style

def display_header():
    instahunter_header = pyfiglet.figlet_format('Instahunter', font='slant')
    print(f'[red]{instahunter_header}')

def get_input():
    return prompt(QUESTIONS, style=pi_custom_style)

def create_json_file(query, json_data):
    file_name = f'instahunter_{query}.json'
    
    try: 
        file = open(file_name, 'w+')
        json.dump(json_data, file, indent=4)
        file.close()
    except:
        raise Exception('Couldn\'t create file.')

    return file_name

def display_data(processed_data):
    formatted_str = json.dumps(processed_data, indent=4)
    print_json(formatted_str)

def display_message(message, success=True):
    if success == True:
        msg_color = 'green'
    else:
        msg_color = 'red'
    print(f'\n[bold {msg_color}]{message}')