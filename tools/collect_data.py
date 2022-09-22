from tqdm import tqdm
from tools.utils import hidden_input, get_project_root
import json
import requests


root = get_project_root()
DATA_LOCATION = root + "/data/data.json"
AVATARS_LOCATION = root + "/data/avatars/"

LINK_API = r"https://discordapp.com/api/v9"


def get_data_friends():
    """ Get data from friends, with id, username, avatarUrl and connections (a list of mutual friends id)

    Raises:
        Exception: Invalid token
        Raise error status if status code is not 200

    Returns:
        dict: data
    """

    TOKEN = hidden_input("Enter your token: ")
    HEADER = {"authorization": TOKEN}

    friends = requests.get(
        rf"{LINK_API}/users/@me/relationships", headers=HEADER)

    # If error to connect to the API
    if friends.status_code == 401:
        raise Exception("Invalid token")
    elif friends.status_code != 200:
        friends.raise_for_status()

    content_friends = friends.json()
    friends = [content_friends[i]["user"] for i in range(len(content_friends))]

    data = dict()

    # Loop through all friends
    for friend in tqdm(friends, desc="collecting friends data"):
        id = friend["id"]
        username = friend["username"]
        avatar = friend["avatar"]
        avatarUrl = rf"https://cdn.discordapp.com/avatars/{id}/{avatar}.png"
        mutual_friends = requests.get(
            rf"{LINK_API}/users/{id}/relationships", headers=HEADER).json()
        mutual_friends_id = [mutual_friend["id"]
                             for mutual_friend in mutual_friends]

        data[id] = {
            "id": id,
            "username": username,
            "avatarUrl": avatarUrl,
            "connections": mutual_friends_id,
        }

    return data


def write_data():
    """Write data of each friend in a big json file
    """
    data = get_data_friends()
    with open(DATA_LOCATION, "w", encoding="utf-8") as f:
        json.dump(data, f)


def download_avatars():
    """Download all avatars of friends in a folder with id as image name
    Returns:
        bool or list : False if no error, list of errors if error to download some images : dict{username: image_url}
    """
    img_errors = dict()

    with open(DATA_LOCATION, "r") as f:
        data = json.load(open(DATA_LOCATION, "r", encoding="utf-8"))

    for user in tqdm(data, desc="Downloading avatars"):
        avatarUrl = data[user]["avatarUrl"]
        avatar = requests.get(avatarUrl)

        if avatar.status_code != 200:
            username = data[user]["username"]
            img_errors[username] = avatarUrl
            continue

        with open(rf"{AVATARS_LOCATION}{user}.png", "wb") as f:
            f.write(avatar.content)

    return False if len(img_errors) == 0 else img_errors


def collect_data():
    write_data()
    img_errors = download_avatars()
    if img_errors:
        print("Errors to download this images :")
        for user, url in img_errors.items():
            print(f"{user}  |  {url}")
