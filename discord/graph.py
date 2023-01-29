import json
import webbrowser
from warnings import warn

import networkx as nx
from bs4 import BeautifulSoup
from pyvis.network import Network

from discord.constants import DATA_FILE_PATH, GRAPH_PATH
from tools.config import DISPLAYED_OPTIONS, expr_size


def create_graph(include_user=False):
    with open(DATA_FILE_PATH, "r") as f:
        data = json.load(f)

    if include_user:
        user_id = next(friend_id for friend_id, friend in data.items() if friend["is_user"])
        for friend in data.values(): # user is not include in connections in data.json by default
            if user_id not in friend["connections"] and friend["id"] != user_id:
                friend["connections"].append(user_id)

    else:
        data = {friend_id: friend for friend_id, friend in data.items() if not friend["is_user"]}

    nodes = []
    for friend in data.values():
        nb_connections = len(friend["connections"])
        nodes.append(
            (
                friend["id"],
                {
                    "label": friend["username"],
                    "title": f"{friend['username']} has {nb_connections} connections",
                    "shape": "circularImage",
                    "image": friend["avatarPath"],
                    "size": expr_size(nb_connections),
                },
            )
        )

    edge_option = {
        "color": {"color": "grey", "highlight": "red"},
        "selectionWidth": 4,
    }

    node_option = {
        "borderWidthSelected": 5,
        "color": {
            "border": "black",
            "highlight": {
                "border": "blue",
            },
        },
        "font": {
            "color": "black",
            "size": 20,
            "face": "arial",
            "strokeWidth": 2,
        },
    }

    edges = []
    for friend in data.values():
        for connection in friend["connections"]:
            edges.append((friend["id"], connection))

    G = nx.Graph()
    G.add_nodes_from(nodes, **node_option)
    G.add_edges_from(edges, **edge_option)

    nt = Network(width="60%")  # Width of 60% to display options buttons on the right of the graph
    nt.from_nx(G)
    if len(DISPLAYED_OPTIONS) > 0:
        nt.show_buttons(filter_=DISPLAYED_OPTIONS)
    nt.toggle_physics(False)  # physics is disabled at the beginning to avoid a big loading time
    nt.barnes_hut(
        gravity=-5000,
        central_gravity=0.3,
        spring_length=20,
        spring_strength=0.01,
        damping=0.09,
        overlap=0,
    )

    return nt


def write_html_graph(nt):
    with open(GRAPH_PATH, "w") as f:
        file = nt.generate_html()
        file = BeautifulSoup(file, "html.parser")
        file_div = file.div
        if file_div is not None:
            file_div.unwrap()  # Modify the html file to display paramters on the right of the graph instead of the bottom
        else:
            warn("The html file was not modified")
        f.write(str(file))


def display_graph(include_user=False):
    nt = create_graph(include_user)
    write_html_graph(nt)
    webbrowser.open("file://" + GRAPH_PATH)


if __name__ == "__main__":
    write_html_graph(create_graph())
