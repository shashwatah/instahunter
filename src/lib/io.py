from termcolor import cprint
import pyfiglet

from PyInquirer import prompt

import json

from lib.utils.question import QUESTIONS, pi_custom_style

def display_header():
    instahunter_header = pyfiglet.figlet_format('Instahunter', font='slant')
    cprint(instahunter_header, 'red')

def get_input():
    return prompt(QUESTIONS, style=pi_custom_style)

def create_json_file(query, json_data):
    file_name = 'instahunter_%s.json'%query
    file = open(file_name, 'w+')
    json.dump(json_data, file, indent=4)
    file.close()
    return file_name

def display_data(processed_data):
    formatted_str = json.dumps(processed_data, indent=4)
    print(formatted_str)