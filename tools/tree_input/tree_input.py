from tools.data_filter import collect_data
from tools.graph import display_graph
from tools.utils import full_input


full_tree = {
    "char": """ What do you want to do ? If it's your first time, you need to collect the data first
                    1. Collect the data
                    2. Create the graph
                    3. Exit
                    """,
    "char_wrong": "Please enter a valid number ( 1 2 3 )",
    "valid": {
        "1": {"char": "Collecting data...", "func": collect_data, "kwargs": {}},
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
