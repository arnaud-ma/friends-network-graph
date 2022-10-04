import os


def check_folder(*folders):
    for folder in folders:
        if not os.path.isdir(folder):
            os.mkdir(folder)


def full_input(char, char_wrong, valid):
    result = input(char)
    if result not in valid:
        print(char_wrong)
        result = full_input(char, char_wrong, valid)
    return result
