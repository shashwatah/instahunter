import click
import requests
import json
from datetime import datetime


@click.group()
def cli():
    """Made by KSSBro | v1.4"""


@click.command()
@click.option('-tag', prompt="Hashtag", help="The hashtag you want to search the posts with")
@click.option('-create-file', default="false", help="true: Create a file with the data | false: Will not create a file, false is default")
@click.option('--file-type', default="text", help="json: Create a json file | text: Create a text file, text is default")
def getposts(tag, create_file, file_type):
    """This command will fetch recent public posts with a Hashtag"""
    try:
        if(create_file == "true"):
            if(file_type == "json"):
                file = open(tag+"_posts.json", "w+")
                json_data = []
            else:
                file = open(tag+"_posts.txt", "w+", encoding="utf-8")
        counter = 0
        api_url = "https://www.instagram.com/explore/tags/%s/?__a=1" % tag
        req = requests.get(url=api_url)
        data = req.json()
        edges = data["graphql"]["hashtag"]["edge_hashtag_to_media"]["edges"]
        for edge in edges:
            counter = counter + 1
            post_id = edge["node"]["id"]
            shortcode = edge["node"]["shortcode"]
            caption = ""
            try:
                caption = edge["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
            except:
                caption = "No Caption"
            ncomments = edge["node"]["edge_media_to_comment"]["count"]
            display_url = edge["node"]["display_url"]
            nlikes = edge["node"]["edge_liked_by"]["count"]
            owner_id = edge["node"]["owner"]["id"]
            is_video = edge["node"]["is_video"]
            time = str(datetime.fromtimestamp(
                edge["node"]["taken_at_timestamp"]))
            if(create_file == "true"):
                if(file_type == "json"):
                    json_data.append({
                        "id": counter,
                        "post_id": post_id,
                        "shortcode": shortcode,
                        "owner_id": owner_id,
                        "display_url": display_url,
                        "caption": caption,
                        "time": time,
                        "n_likes": nlikes,
                        "n_comments": ncomments,
                        "is_video": is_video
                    })
                else:
                    file.write("###############################\nID: %s \nPost ID: %s \nShortcode: %s \nOwner ID: %s \nDisplay URL: %s \nCaption: %s \nTime: %s \nNumber of likes: %s \nNumber of comments: %s \nIs Video: %s \n###############################\n\n\n\n\n" % (
                        str(counter), str(post_id), str(shortcode), str(owner_id), str(display_url), str(caption), str(time), str(nlikes), str(ncomments), str(is_video)))
            else:
                click.echo("###############################\nNumber: %s \nPost ID: %s \nShortcode: %s \nOwner ID: %s \nImage URL: %s \nCaption: %s \nTime: %s \nNumber of likes: %s \nNumber of comments: %s \nIs Video: %s \n###############################\n\n\n\n\n" % (
                    counter, post_id, shortcode, owner_id, display_url, caption, time, nlikes, ncomments, is_video))
        if(create_file == "true"):
            if(file_type == "json"):
                json.dump(json_data, file)
                click.echo("File Created, name: '%s_posts.json'" % tag)
            else:
                click.echo("File Created, name: '%s_posts.txt" % tag)
            file.close()
        else:
            click.echo("Done!")
    except:
        click.echo(
            "Couldn't retrieve data, One of the following was the issue: \n1. Your query was wrong \n2. Instagram servers did not respond \n3. There is a problem with your internet connection")


@click.command()
@click.option('-via', prompt="Via", default="username", help="username: search user by Username | id: search user by ID")
@click.option('--value', prompt="Value", help='Username or ID you want to search the user by')
@click.option('-create-file', default="false", help="true: Create a file with the data | false: Will not create a file, false is default")
@click.option('--file-type', default="text", help="json: Create a json file | text: Create a text file, text is default")
def getuser(via, value, create_file, file_type):
    """This command will fetch user data with a Username or ID"""
    if(via == "id"):
        api_url = "https://i.instagram.com/api/v1/users/%s/info" % value
    elif(via == "username"):
        api_url = "https://www.instagram.com/%s/?__a=1" % value
    try:
        req = requests.get(url=api_url)
        data = req.json()
        if(via == "id"):
            user = data["user"]
            profile_pic_url = user["hd_profile_pic_url_info"]["url"]
            uploads = user["media_count"]
            followers = user["follower_count"]
            following = user["following_count"]
            tags_following = user["following_tag_count"]
            igtv_videos = user["total_igtv_videos"]
            tagged = user["usertags_count"]
            has_highlights = user["has_highlight_reels"]
            user_id = user["pk"]
        elif(via == "username"):
            user = data["graphql"]["user"]
            profile_pic_url = user["profile_pic_url_hd"]
            uploads = user["edge_owner_to_timeline_media"]["count"]
            followers = user["edge_followed_by"]["count"]
            following = user["edge_follow"]["count"]
            tags_following = "Search by ID!"
            igtv_videos = user["edge_felix_video_timeline"]["count"]
            tagged = "Search by ID!"
            if(user["highlight_reel_count"] > 0):
                has_highlights = True
            else:
                has_highlights = False
            user_id = user["id"]
        username = user["username"]
        full_name = user["full_name"]
        is_private = user["is_private"]
        is_verified = user["is_verified"]
        bio = user["biography"]
        external_url = user["external_url"]
        if(create_file == "true"):
            if(file_type == "json"):
                file = open(value+"_user.json", "w+")
                json.dump({
                    "user_id": user_id,
                    "username": username,
                    "full_name": full_name,
                    "profile_pic_url": profile_pic_url,
                    "bio": bio,
                    "n_uploads": uploads,
                    "n_followers": followers,
                    "n_following": following,
                    "private_id": is_private,
                    "verified_id": is_verified,
                    "tags_following": tags_following,
                    "external_url": external_url,
                    "igtv_videos": igtv_videos,
                    "n_tagged": tagged,
                    "has_highlights": has_highlights
                }, file)
                file.close()
                click.echo("File Created, name: '%s_user.json'" % str(value))
            else:
                file = open(value+"_user.txt", "w+", encoding="utf-8")
                file.write("User ID: %s \nUsername: %s \nFull Name: %s \nProfile Pic URL: %s \nBio: %s \nUploads: %s \nFollowers: %s \nFollowing: %s \nPrivate ID: %s \nVerified ID: %s \nTags following: %s \nExternal URL: %s \nIGTV videos: %s \nTimes user was tagged: %s \nHas highlights: %s" % (
                    str(user_id), username, full_name, profile_pic_url, bio, str(uploads), str(followers), str(following), str(is_private), str(is_verified), str(tags_following), external_url, str(igtv_videos), str(tagged), str(has_highlights)))
                file.close()
                click.echo("File Created, name: '%s_user.txt'" % str(value))
        else:
            click.echo("User ID: %s \nUsername: %s \nFull Name: %s \nProfile Pic URL: %s \nBio: %s \nUploads: %s \nFollowers: %s \nFollowing: %s \nPrivate ID: %s \nVerified ID: %s \nTags following: %s \nExternal URL: %s \nIGTV videos: %s \nTimes user was tagged: %s \nHas highlights: %s" % (
                str(user_id), username, full_name, profile_pic_url, bio, str(uploads), str(followers), str(following), str(is_private), str(is_verified), str(tags_following), external_url, str(igtv_videos), str(tagged), str(has_highlights)))
            click.echo('Done!')
    except:
        click.echo(
            "Couldn't retrieve data, One of the following was the issue: \n1. Your query was wrong \n2. Instagram servers did not respond \n3. There is a problem with your internet connection")


@click.command()
@click.option('-username', prompt="Username", help='The username of the user you want to search the user id of')
@click.option('-create-file', default="false", help="true: Create a file with the data | false: Will not create a file, false is default")
@click.option('--file-type', default="text", help="json: Create a json file | text: Create a text file, text is default")
def getuserposts(username, create_file, file_type):
    """This command will fetch recent posts of a user with a Username"""
    try:
        if(create_file == "true"):
            if(file_type == "json"):
                file = open(username+"_posts.json", "w+")
                json_data = []
            else:
                file = open(username+"_posts.txt", "w+", encoding="utf-8")
        counter = 0
        api_url = "https://www.instagram.com/%s/?__a=1" % username
        req = requests.get(url=api_url)
        data = req.json()
        posts = data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
        for post in posts:
            counter = counter + 1
            node = post["node"]
            post_id = node["id"]
            try:
                caption = node["edge_media_to_caption"]["edges"][0]["node"]["text"]
            except:
                caption = ""
            shortcode = node["shortcode"]
            ncomments = node["edge_media_to_comment"]["count"]
            comments_disabled = node["comments_disabled"]
            time = str(datetime.fromtimestamp(node["taken_at_timestamp"]))
            height = node["dimensions"]["height"]
            width = node["dimensions"]["width"]
            display_url = node["display_url"]
            nlikes = node["edge_liked_by"]["count"]
            try:
                location = node["location"]["name"]
            except:
                location = "No Location"
            is_video = node["is_video"]
            if(create_file == "true"):
                if(file_type == "json"):
                    json_data.append({
                        "id": counter,
                        "post_id": post_id,
                        "shortcode": shortcode,
                        "display_url": display_url,
                        "height": height,
                        "width": width,
                        "caption": caption,
                        "time": time,
                        "nlikes": nlikes,
                        "comments_disabled": comments_disabled,
                        "ncomments": ncomments,
                        "location": location,
                        "is_video": is_video
                    })
                else:
                    file.write("###############################\nID: %s \nPost ID: %s \nShortcode: %s \nDisplay URL: %s \nImage Height: %s \nImage Width: %s \nCaption: %s \nTime: %s \nNumber of likes: %s \nComments Disabled: %s \nNumber of comments: %s \nLocation: %s \nIs Video: %s \n###############################\n\n\n\n\n" % (
                        str(counter), str(post_id), str(shortcode), str(display_url), str(height), str(width), str(caption), str(time), str(nlikes), str(comments_disabled), str(ncomments), str(location), str(is_video)))
            else:
                click.echo("###############################\nID: %s \nPost ID: %s \nShortcode: %s \nDisplay URL: %s \nImage Height: %s \nImage Width: %s \nCaption: %s \nTime: %s \nNumber of likes: %s \nComments Disabled: %s \nNumber of comments: %s \nLocation: %s \nIs Video: %s \n###############################\n\n\n\n\n" % (
                    counter, post_id, shortcode, display_url, height, width, caption, time, nlikes, comments_disabled, ncomments, location, is_video))
        if(create_file == "true"):
            if(file_type == "json"):
                json.dump(json_data, file)
                click.echo("File Created, name: '%s_posts.json'" % username)
            else:
                click.echo("File Created, name: '%s_posts.txt" % username)
            file.close()
        else:
            click.echo("Done!")
    except:
        click.echo(
            "Couldn't retrieve data, One of the following was the issue: \n1. Your query was wrong \n2. Instagram servers did not respond \n3. There is a problem with your internet connection")


cli.add_command(getposts)
cli.add_command(getuser)
cli.add_command(getuserposts)

if __name__ == "__main__":
    cli()
