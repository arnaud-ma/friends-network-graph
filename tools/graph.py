import json
import webbrowser
import networkx as nx
from bs4 import BeautifulSoup
from pyvis.network import Network
from tools.config import expr_size
from tools.config import GRAPH_PATH, DATA_FILE_PATH, DISPLAYED_OPTIONS

def create_graph(include_user=False):
    with open(DATA_FILE_PATH, "r") as f:
        data = json.load(f)

    if not include_user:
        data = {friend_id: friend for friend_id, friend in data.items() if not friend["is_user"]}

    nodes = []
    for friend in data.values():
        nb_connections = len(friend["connections"]) + 1
        nodes.append(
            (
                friend["id"],
                {
                    "label": friend["username"],
                    "title": f"{friend['username']} has {nb_connections} connections",
                    "shape": "circularImage",
                    "image": friend["avatarUrl"],
                    "size": expr_size(nb_connections),
                },
            )
        )

    edge_option = {"color": {"color": "grey", "highlight": "red"}, "font": "20px arial black"}

    edges = [
        (friend["id"], connection)
        for friend in data.values()
        for connection in friend[
            "connections"
        ]  # tuple of (friend_id, connection_id) for each connection
    ]

    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges, **edge_option)

    nt = Network(width="60%")  # Width of 60% to display options buttons on the right of the graph
    nt.from_nx(G)
    if len(DISPLAYED_OPTIONS) > 0:
        nt.show_buttons(filter_=DISPLAYED_OPTIONS)
    nt.toggle_physics(False)  # physics is disabled at the beginning to avoid a big loading time

    return nt


def write_html_graph(nt):
    with open(GRAPH_PATH, "w") as f:
        file = nt.generate_html()
        file = BeautifulSoup(file, "html.parser")
        file.div.unwrap()
        f.write(str(file))


def connect():
    webbrowser.open("file://" + GRAPH_PATH)


def graph(include_user=False):
    nt = create_graph(include_user)
    write_html_graph(nt)
    connect()
