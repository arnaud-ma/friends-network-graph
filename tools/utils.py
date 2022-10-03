import platform
from getpass import getpass
from pwinput import pwinput
import os


def hidden_input(str, char="*"):
    """Hide input

    Args:
        str (str): Text to display
        char (str, optional): Only on Windows. Character to hide. Defaults to "*".

    Returns:
        str: Input
    """
    if platform.system() == "Windows":
        return pwinput(prompt=str, mask=char)
    else:
        return getpass(str)


def check_folder(*folders):
    for folder in folders:
        if not os.path.isdir(folder):
            os.mkdir(folder)
