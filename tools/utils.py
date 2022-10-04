import os


def check_folder(*folders):
    for folder in folders:
        if not os.path.isdir(folder):
            os.mkdir(folder)
