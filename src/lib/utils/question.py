from PyInquirer import style_from_dict, Token, Validator, ValidationError
import regex

# regex source: https://stackoverflow.com/a/64910992/14477608
class UsernameTagValidator(Validator):
    def validate(self, document):
        ok = regex.match('^[\w](?!.*?\.{2})[\w.]{1,28}[\w]$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid query',
                cursor_position=len(document.text))

def show_post_options(input):
    if input['query_type'] == 'posts':
        return True
    else:
        return False

QUESTIONS = [
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
        'message': 'Query:',
        'validate': UsernameTagValidator
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
        'when': show_post_options
    },
    {
        'type': 'confirm',
        'name': 'file_confirm',
        'message': 'Do you want to output the results to a JSON file?'
    }
]

pi_custom_style = style_from_dict({
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',
    Token.Pointer: '#673ab7 bold',
    Token.Answer: '#f44336 bold',
})