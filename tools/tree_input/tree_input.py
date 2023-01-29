from discord.data_filter.fetch_data import fetch_data
from discord.graph import display_graph
from tools.utils import full_input

full_tree = {
    "char": (
        "\n What do you want to do ? If it's your first time, you need to collect the data first \n"
        "\t 1. Collect the data \n"
        "\t 2. Create the graph \n"
        "\t 3. Exit \n"
    ),
    "char_wrong": "Please enter a valid number ( 1 2 3 )",
    "valid": {
        "1": {"char": "Collecting data...", "func": fetch_data, "kwargs": {}},
        "2": {
            "char": "Do you want to include yourself in the graph ? (y/n) ",
            "char_wrong": "Please enter a valid answer (y/n)",
            "valid": {
                "y": {
                    "char": "Creating graph...",
                    "func": display_graph,
                    "kwargs": {"include_user": True},
                },
                "n": {
                    "char": "Creating graph...",
                    "func": display_graph,
                    "kwargs": {"include_user": False},
                },
            },
        },
        "3": {"char": "Exiting...", "func": exit, "kwargs": {}},
    },
}


def display_tree(tree):
    if "valid" in tree:
        char, char_wrong, valid = tree.values()
        result = full_input(char, char_wrong, valid)
        tree = tree["valid"][result]
    else:
        char, func, kwargs = tree.values()
        print(char)
        func(**kwargs)
        tree = full_tree

    display_tree(tree)
