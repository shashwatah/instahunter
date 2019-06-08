import click
import requests


@click.group()
def cli():
    pass


@click.command()
@click.option('--tag', prompt="Hashtag", help="The hashtags you want to search the posts with")
@click.option('--create-file', default="false", help="If you want to create a file with the data then write true")
def getposts(tag, create_file):
    if(create_file == "true"):
        file = open("data.txt", "w+", encoding="utf-8")
    counter = 0
    apiUrl = "https://www.instagram.com/explore/tags/%s/?__a=1" % tag
    req = requests.get(url=apiUrl)
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
            file.write("###############################\nNumber: %s \nPost ID: %s \nShortcode: %s \nOwner ID: %s \nImage URL: %s \nCaption: %s \nNumber of likes: %s \nNumber of comments: %s \n###############################\n\n\n\n\n" % (
                str(counter), str(post_id), str(shortcode), str(owner_id), str(image_url), str(caption), str(nlikes), str(ncomments)))
        else:
            click.echo("###############################\nNumber: %s \nPost ID: %s \nShortcode: %s \nOwner ID: %s \nImage URL: %s \nCaption: %s \nNumber of likes: %s \nNumber of comments: %s \n###############################\n\n\n\n\n" % (
                counter, post_id, shortcode, owner_id, image_url, caption, nlikes, ncomments))
    if(create_file == "true"):
        click.echo("File Created")
        file.close()
    else:
        click.echo("Done!")


@click.command()
@click.option('--userid', prompt="User ID", help='The User ID you want to search the user by')
def getuser(userid):
    click.echo(userid)


cli.add_command(getposts)
cli.add_command(getuser)

if __name__ == "__main__":
    cli()
