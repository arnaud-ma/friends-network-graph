import requests
from tools.config import LINK_API


def get_data_from_api(url, header):
    """Get data from API

    Args:
        url (str): URL to get data
        header (dict): Header

    Raises:
        Exception: Invalid token
        Raise error status if status code is not 200

    Returns:
        dict: data
    """
    data = requests.get(url, headers=header)

    # If error to connect to the API
    if data.status_code == 401:
        raise Exception("Invalid token")
    elif data.status_code != 200:
        data.raise_for_status()

    return data.json()


def filter_friend_data(raw_friend, data, header, is_user=False):
    """Filter raw data of a user to get only what we want

    Args:
        raw_friend (dict): raw data of a friend
        data (dict): data to add content
        user(bool, optionnal): True if it's the only user, False if it's a friend
        header (dict): Header

    Returns:
        dict[id, username, avatar, avatarUrl, connections]: data of friends
    """

    id = raw_friend["id"]
    username = raw_friend["username"]
    avatar = raw_friend["avatar"]
    avatarUrl = rf"https://cdn.discordapp.com/avatars/{id}/{avatar}.png"
    mutual_friends = get_data_from_api(rf"{LINK_API}/users/{id}/relationships", header)
    mutual_friends_id = [mutual_friend["id"] for mutual_friend in mutual_friends]

    data[id] = {
        "id": id,
        "username": username,
        "is_user": is_user,
        "avatarUrl": avatarUrl,
        "connections": mutual_friends_id,
    }

    return data
