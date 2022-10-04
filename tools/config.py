import os
import math

# Api
LINK_API = "https://discordapp.com/api/v9"

# Path
ROOT = os.path.dirname(os.path.realpath("start.py"))
DATA_PATH = ROOT + "/data"
DATA_FILE_PATH = ROOT + "/data/data.json"
AVATARS_PATH = ROOT + "/data/avatars/"
GRAPH_PATH = ROOT + "/graph.html"


""" Options displayed on the page. There can be "physics", "nodes", "edges", "interaction", "layout", "configure" and "navigation" """
DISPLAYED_OPTIONS = [
    "physics",
]


# Size of a node in function of the number of connections
def expr_size(x):
    return 10 * math.sqrt(x) + 1
