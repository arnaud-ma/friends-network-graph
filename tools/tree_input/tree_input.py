from sys import exit

from discord.data_filter.fetch_data import fetch_data as discord_fetch_data
from discord.graph import display_graph as discord_display_graph
from tools.utils import full_input

full_tree = {
    "char": "Which app do you want to use ? \n" "\t 1. discord \n",
    "char_wrong": "Please enter a valid number ( 1 )",
    "valid": {
        "1": {
            "char": (
                "\n What do you want to do ? If it's your first time, you need to collect the data first \n"
                "\t 1. Collect the data \n"
                "\t 2. Create the graph \n"
                "\t 3. Exit \n"
            ),
            "char_wrong": "Please enter a valid number ( 1 2 3 )",
            "valid": {
                "1": {
                    "char": "Collecting data...",
                    "func": discord_fetch_data,
                    "args": [],
                    "kwargs": {},
                },
                "2": {
                    "char": "Do you want to include yourself in the graph ? (y/n) ",
                    "char_wrong": "Please enter a valid answer (y/n)",
                    "valid": {
                        "y": {
                            "char": "Creating graph...",
                            "func": discord_display_graph,
                            "args": [],
                            "kwargs": {"include_user": True},
                        },
                        "n": {
                            "char": "Creating graph...",
                            "func": discord_display_graph,
                            "args": [],
                            "kwargs": {"include_user": False},
                        },
                    },
                },
                "3": {"char": "Exiting...", "func": exit, "args": [0], "kwargs": {}},
            },
        }
    },
}


def display_tree(tree):
    if "valid" in tree:
        char, char_wrong, valid = tree.values()
        result = full_input(char, char_wrong, valid)
        tree = tree["valid"][result]
    else:
        char, func, args, kwargs = tree.values()
        print(char)
        func(*args, **kwargs)
        tree = full_tree

    display_tree(tree)
