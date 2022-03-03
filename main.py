import os
import requests 
from datetime import datetime

from PyInquirer import prompt, style_from_dict, Token

from termcolor import cprint
import pyfiglet

os.system('color')

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

def get_posts(tag, post_type):
    api_url = "https://www.instagram.com/explore/tags/%s/?__a=1" % tag
    request = requests.get(url=api_url, headers=headers)
    raw_data = request.json()

    return process_posts(raw_data, post_type)

def process_posts(raw_data, post_type):
    processed_data = []
    counter = 0

    if(post_type == "top"):
        edges = raw_data["graphql"]["hashtag"]["edge_hashtag_to_top_posts"]["edges"]
    else:
        edges = raw_data["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"]

    for edge in edges:
        counter += 1
       
        try:
            caption = edge["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
        except:
            caption = "No Caption"

        processed_data.append({
            "id": counter,
            "post_id": edge["node"]["id"],
            "shortcode": edge["node"]["shortcode"],
            "owner_id": edge["node"]["owner"]["id"],
            "display_url": edge["node"]["display_url"],
            "caption": caption,
            "time": str(datetime.fromtimestamp(
                edge["node"]["taken_at_timestamp"])),
            "n_likes": edge["node"]["edge_liked_by"]["count"],
            "n_comments": edge["node"]["edge_media_to_comment"]["count"],
            "is_video": edge["node"]["is_video"]
        })

    return processed_data

def get_user_data(username):
    api_url = "https://www.instagram.com/%s/?__a=1" % username
    request = requests.get(url=api_url, headers=headers)
    raw_data = request.json()

    return process_user_data(raw_data)

def process_user_data(raw_data):
    user_data = raw_data["graphql"]["user"]

    if(user_data["highlight_reel_count"] > 0):
        has_highlights = True
    else:
        has_highlights = False

    return {
        "user_id": user_data["id"],
        "username": user_data["username"],
        "full_name": user_data["full_name"],
        "profile_pic_url": user_data["profile_pic_url_hd"],
        "bio": user_data["biography"],
        "n_uploads": user_data["edge_owner_to_timeline_media"]["count"],
        "n_followers": user_data["edge_followed_by"]["count"],
        "n_following": user_data["edge_follow"]["count"],
        "is_private": user_data["is_private"],
        "is_verified": user_data["is_verified"],
        "external_url": user_data["external_url"],
        "igtv_videos": user_data["edge_felix_video_timeline"]["count"],
        "has_highlights": has_highlights
    }

def get_user_posts(username):
    api_url = "https://www.instagram.com/%s/?__a=1" % username
    request = requests.get(url=api_url, headers=headers)
    raw_data = request.json()

    return process_user_posts(raw_data)

def process_user_posts(raw_data):
    processed_data = []
    counter = 0

    post_edges = raw_data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]

    for post in post_edges:
        counter  += 1
        post_node = post["node"]

        try:
            caption = post_node["edge_media_to_caption"]["edges"][0]["node"]["text"]
        except:
            caption = ""

        try:
            location = post_node["location"]["name"]
        except:
            location = "No Location"

        processed_data.append({
            "id": counter,
            "post_id": post_node["id"],
            "shortcode": post_node["shortcode"],
            "display_url": post_node["display_url"],
            "height": post_node["dimensions"]["height"],
            "width": post_node["dimensions"]["width"],
            "caption": caption,
            "time": str(datetime.fromtimestamp(post_node["taken_at_timestamp"])),
            "n_likes": post_node["edge_liked_by"]["count"],
            "comments_disabled": post_node["comments_disabled"],
            "n_comments": post_node["edge_media_to_comment"]["count"],
            "location": location,
            "is_video": post_node["is_video"]
        })

    return processed_data

def get_search_results(query):
    api_url = "https://www.instagram.com/web/search/topsearch/?query=%s" % query
    request = requests.get(api_url, headers=headers)
    raw_data = request.json()

    return process_search_results(raw_data)

def process_search_results(raw_data):
    processed_data = []
    counter = 0
    
    for user in raw_data["users"]:
        counter += 1

        processed_data.append({
            "id": counter,
            "user_id": user["user"]["pk"],
            "username": user["user"]["username"],
            "full_name": user["user"]["full_name"],
            "profile_pic_url": user["user"]["profile_pic_url"],
            "is_private": user["user"]["is_private"],
            "is_verified": user["user"]["is_verified"],
        })

    return processed_data

pi_custom_style = style_from_dict({
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',
    Token.Pointer: '#673ab7 bold',
    Token.Answer: '#f44336 bold',
})


instahunter_header = pyfiglet.figlet_format('Instahunter', font='slant')
cprint(instahunter_header, 'red', attrs=['blink'])

questions = [
    {
        'type': 'list',
        'name': 'querytype',
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