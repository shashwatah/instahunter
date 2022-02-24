import os
import requests 
import json 

from PyInquirer import prompt, Separator, style_from_dict, Token

from termcolor import cprint
import pyfiglet

os.system('color')

pi_custom_style = style_from_dict({
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',
    Token.Pointer: '#673ab7 bold',
    Token.Answer: '#f44336 bold',
})

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

instahunter_header = pyfiglet.figlet_format('Instahunter', font='slant')
cprint(instahunter_header, 'red', attrs=['blink'])



questions = [
    {
        'type': 'list',
        'name': 'type',
        'message': 'What do you want to lookup?',
        'choices': [
            'Public Posts',
            'User Data',
            'User Posts',
            'Search Results'
        ]
    }
]

answers = prompt(questions, style=pi_custom_style)
print(answers)

# api endpoints:
# posts:      https://www.instagram.com/explore/tags/*tag*/?__a=1
# user data:  https://www.instagram.com/*username*/?__a=1
# user posts: https://www.instagram.com/*username*/?__a=1
# search:     https://www.instagram.com/web/search/topsearch/?query=*query*" 

