from datetime import datetime 

def process_posts(raw_data, post_type):
    print("process posts func")
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

process_func_dispatcher = {
    'posts': process_posts,
    'user_data': process_user_data,
    'user_posts': process_user_posts,
    'search': process_search_results
}
