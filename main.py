from PyInquirer import prompt, style_from_dict, Token

from termcolor import cprint
import pyfiglet

from lib.controller import main_controller

pi_custom_style = style_from_dict({
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',
    Token.Pointer: '#673ab7 bold',
    Token.Answer: '#f44336 bold',
})

instahunter_header = pyfiglet.figlet_format('Instahunter', font='slant')
cprint(instahunter_header, 'red')

def get_post_options(answers):
    if answers['query_type'] == 'posts':
        return True
    else:
        return False

questions = [
    {
        'type': 'list',
        'name': 'query_type',
        'message': 'What do you want to lookup?',
        'choices': [
            {
                'name': 'Public Posts',
                'value': 'posts'
            },
            {
                'name': 'User Data',
                'value': 'user_data'
            },
            {
                'name': 'User Posts',
                'value': 'user_posts'
            },
            {
                'name': 'Search Results',
                'value': 'search'
            }
        ]
    },
    {
        'type': 'input',
        'name': 'query',
        'message': 'Query:'
    },
    {
        'type': 'list',
        'name': 'post_type',
        'message': 'What kind of posts are you looking for?',
        'choices': [
            {
                'name': 'Top',
                'value': 'top'
            },
            {
                'name': 'Latest',
                'value': 'latest'
            }
        ],
        'when': get_post_options
    },
    {
        'type': 'confirm',
        'name': 'file_confirm',
        'message': 'Do you want to output the results to a JSON file?'
    }
]

answers = prompt(questions, style=pi_custom_style)

main_controller(answers)

print(answers)