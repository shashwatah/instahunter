import click
import requests
import json


@click.group()
def cli():
    """Made by KSSBro | v1.1"""


@click.command()
@click.option('-tag', prompt="Hashtag", help="The hashtag you want to search the posts with")
@click.option('-create-file', default="false", help="true: Create a file with the data | false: Will not create a file, false is default")
@click.option('--file-type', default="text", help="json: Create a json file | text: Create a text file, text is default")
def getposts(tag, create_file, file_type):
    """This command will help you get posts by entering a hashtag"""
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
            image_url = edge["node"]["display_url"]
            nlikes = edge["node"]["edge_liked_by"]["count"]
            owner_id = edge["node"]["owner"]["id"]
            if(create_file == "true"):
                if(file_type == "json"):
                    json_data.append({
                        "Number": counter,
                        "Post ID": post_id,
                        "Shortcode": shortcode,
                        "Owner ID": owner_id,
                        "Image URL": image_url,
                        "Caption": caption,
                        "Number of likes": nlikes,
                        "Number of Comments": ncomments
                    })
                else:
                    file.write("###############################\nNumber: %s \nPost ID: %s \nShortcode: %s \nOwner ID: %s \nImage URL: %s \nCaption: %s \nNumber of likes: %s \nNumber of comments: %s \n###############################\n\n\n\n\n" % (
                        str(counter), str(post_id), str(shortcode), str(owner_id), str(image_url), str(caption), str(nlikes), str(ncomments)))
            else:
                click.echo("###############################\nNumber: %s \nPost ID: %s \nShortcode: %s \nOwner ID: %s \nImage URL: %s \nCaption: %s \nNumber of likes: %s \nNumber of comments: %s \n###############################\n\n\n\n\n" % (
                    counter, post_id, shortcode, owner_id, image_url, caption, nlikes, ncomments))
        if(create_file == "true"):
            if(file_type == "json"):
                json.dump(json_data, file)
                click.echo("File Created, name: '%s_posts.json'" % tag)
            else:
                click.echo("File Create, name: '%s_posts.txt" % tag)
            file.close()
        else:
            click.echo("Done!")
    except:
        click.echo(
            "Couldn't retrieve data, either the servers did not respond or there is a problem with your connection")


@click.command()
@click.option('-user-id', prompt="User ID", help='The User ID you want to search the user by')
@click.option('-create-file', default="false", help="true: Create a file with the data | false: Will not create a file, false is default")
@click.option('--file-type', default="text", help="json: Create a json file | text: Create a text file, text is default")
def getuser(user_id, create_file, file_type):
    """This command will help you get user data by entering user id"""
    try:
        api_url = "https://i.instagram.com/api/v1/users/%s/info" % user_id
        req = requests.get(url=api_url)
        data = req.json()
        user = data["user"]
        username = user["username"]
        full_name = user["full_name"]
        is_private = user["is_private"]
        profile_pic_url = user["hd_profile_pic_versions"][0]["url"]
        is_verified = user["is_verified"]
        uploads = user["media_count"]
        followers = user["follower_count"]
        following = user["following_count"]
        bio = user["biography"]
        if(create_file == "true"):
            if(file_type == "json"):
                file = open(user_id+"_user.json", "w+")
                json.dump({
                    "Username": username,
                    "Full Name": full_name,
                    "Profile Pic URL": profile_pic_url,
                    "Bio": bio,
                    "Uploads": uploads,
                    "Followers": followers,
                    "Following": following,
                    "Private ID": is_private,
                    "Verified ID": is_verified
                }, file)
                file.close()
                click.echo("File Created, name: '%s_user.json'" % str(user_id))
            else:
                file = open(user_id+"_user.txt", "w+", encoding="utf-8")
                file.write("Username: %s \nFull Name: %s \nProfile Pic URL: %s \nBio: %s \nUploads: %s \nFollowers: %s \nFollowing: %s \nPrivate ID: %s \nVerified ID: %s" % (
                    username, full_name, profile_pic_url, bio, str(uploads), str(followers), str(following), str(is_private), str(is_verified)))
                file.close()
                click.echo("File Created, name: '%s_user.txt'" % str(user_id))
        else:
            click.echo("Username: %s \nFull Name: %s \nProfile Pic Url: %s \nBio: %s \nUploads: %s \nFollowers: %s \nFollowing: %s \nPrivate ID: %s \nVerified ID: %s" % (
                username, full_name, profile_pic_url, bio, str(uploads), str(followers), str(following), str(is_private), str(is_verified)))
            click.echo('Done!')
    except:
        click.echo(
            "Couldn't retrieve data, either the servers did not respond or there is a problem with your connection")


@click.command()
@click.option('-username', prompt="Username", help='The username of the user you want to search the user id of')
@click.option('-create-file', default="false", help="true: Create a file with the data | false: Will not create a file, false is default")
@click.option('--file-type', default="text", help="json: Create a json file | text: Create a text file, text is default")
def getuserid(username, create_file, file_type):
    """This command will help you get user id by entering username"""
    try:
        api_url = "https://www.instagram.com/%s/?__a=1" % username
        req = requests.get(url=api_url)
        data = req.json()
        user_id = data["graphql"]["user"]["id"]
        if(create_file == "true"):
            if(file_type == "json"):
                file = open(username+"_user_id.json", "w+")
                json.dump({
                    "Username": username,
                    "User ID": user_id
                }, file),
                file.close()
                click.echo("File Created, name: '%s_user_id.json'" % username)
            else:
                file = open(username+"_user_id.txt", "w+", encoding="utf-8")
                file.write("User ID for username '%s': %s" % (
                    username, user_id))
                file.close()
                click.echo("File Created, name: '%s_user_id.txt'" % username)
        else:
            click.echo("User ID for username '%s': %s" % (username, user_id))
            click.echo("Done!")
    except:
        click.echo(
            "Couldn't retrieve data, either the servers did not respond or there is a problem with your connection")


cli.add_command(getposts)
cli.add_command(getuser)
cli.add_command(getuserid)

if __name__ == "__main__":
    cli()
