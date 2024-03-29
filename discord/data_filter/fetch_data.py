import json

import requests
from pwinput import pwinput
from tqdm import tqdm

from discord.constants import API_LINK, AVATARS_PATH, DATA_FILE_PATH, FOLDER
from tools.utils import check_folder

from .utils_data import filter_friend_data, get_data_from_api


def get_data_friends():
    """Get data from friends, with id, username, avatarUrl and connections (a list of mutual friends id)

    Returns:
        dict: data
    """

    TOKEN = pwinput("Enter your token: ", mask="*")
    HEADER = {"authorization": TOKEN}

    content_friends = get_data_from_api(rf"{API_LINK}/users/@me/relationships", HEADER)
    friends = [content_friends[i]["user"] for i in range(len(content_friends))]

    data = dict()

    # Loop through all friends
    for friend in tqdm(friends, desc="fetching friends data"):
        data = filter_friend_data(friend, data, HEADER)
    all_friends = set(data.keys())
    # Add the user
    user = get_data_from_api(rf"{API_LINK}/users/@me", HEADER)
    data = filter_friend_data(user, data, HEADER, is_user=True)

    # Fix a bug where friends are in /users/@me/relationships but not in /users/@me
    connections_user = set(data[user["id"]]["connections"]) | all_friends
    data[user["id"]]["connections"] = list(connections_user)

    return data


def write_data():
    """Write data of each friend in a big json file"""
    check_folder(FOLDER)
    data = get_data_friends()
    with open(DATA_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f)


def download_avatars():
    """Download all avatars of friends in a folder with id as image name
    Returns:
        bool or list : False if no error, list of errors if error to download some images : dict{username: image_url}
    """
    check_folder(FOLDER, AVATARS_PATH)
    img_errors = dict()
    with open(DATA_FILE_PATH, "r") as f:
        data = json.load(open(DATA_FILE_PATH, "r", encoding="utf-8"))

    for user in tqdm(data, desc="Downloading avatars"):
        avatarUrl = data[user]["avatarUrl"]
        avatar = requests.get(avatarUrl)

        if avatar.status_code != 200:
            username = data[user]["username"]
            img_errors[username] = avatarUrl
            continue

        with open(rf"{AVATARS_PATH}{user}.png", "wb") as f:
            f.write(avatar.content)

    return False if len(img_errors) == 0 else img_errors


def fetch_data():
    write_data()
    img_errors = download_avatars()
    if img_errors:
        print("Errors to download this images :")
        for user, url in img_errors.items():
            print(f"{user}  |  {url}")
