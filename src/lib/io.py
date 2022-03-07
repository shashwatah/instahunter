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

def display_data(processed_data):
    formatted_str = json.dumps(processed_data, indent=2)
    print(formatted_str)