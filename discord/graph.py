import json
import webbrowser
from warnings import warn

import networkx as nx
from bs4 import BeautifulSoup
from pyvis.network import Network

from discord.constants import DATA_FILE_PATH, GRAPH_PATH
from tools.config import DISPLAYED_OPTIONS, expr_size


def load_data():
    """Load data from data.json file"""
    with open(DATA_FILE_PATH, "r") as f:
        data = json.load(f)
    return data


def include_user_in_data(data: dict) -> dict:
    """Add user to data.json file"""
    user_id = next(friend_id for friend_id, friend in data.items() if friend["is_user"])
    for friend in data.values():  # user is not include in connections in data.json by default
        if user_id not in friend["connections"] and friend["id"] != user_id:
            friend["connections"].append(user_id)
    return data


def exclude_user_from_data(data: dict) -> dict:
    """Remove user from data.json file"""
    data = {friend_id: friend for friend_id, friend in data.items() if not friend["is_user"]}
    return data


def create_nodes(data: dict, include_user: bool = False) -> list:
    """Create nodes from data.json file"""
    nodes = []
    for friend in data.values():
        nb_connections = len(friend["connections"])
        if not include_user:
            nb_connections += 1
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
    return nodes


def create_edges(data: dict) -> list:
    """Create edges from data.json file"""
    edges = []
    for friend in data.values():
        for connection in friend["connections"]:
            edges.append((friend["id"], connection))
    return edges


def create_graph(include_user=False):
    data = load_data()

    if include_user:
        data = include_user_in_data(data)
    else:
        data = exclude_user_from_data(data)

    nodes = create_nodes(data, include_user)
    edges = create_edges(data)

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
