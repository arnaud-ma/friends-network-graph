import os
import math

apps = ["discord"]

# Api
API_LINKS = {
    "discord": "https://discord.com/api/v9",
}

# Paths
ROOT = os.path.dirname(os.path.realpath("start.py"))
DATA_FOLDER = ROOT + "/data"

paths = dict()
for app in apps:
    folder = DATA_FOLDER + "/" + app
    paths[app] = {
        "folder": folder,
        "data_file_path": folder + "/data.json",
        "avatars_path":   folder + "/avatars/",
        "graph_path":     folder + "/graph.html",
    }


""" Options displayed on the page. There can be "physics", "nodes", "edges", "interaction", "layout", "configure" and "navigation" """
DISPLAYED_OPTIONS = [
    "physics",
]


# Size of a node in function of the number of connections
def expr_size(x):
    return 10 * math.sqrt(x) + 1
