
# Social-network-graph

 Create a network graph of your friends on a social media.  
 Inspired by [humboldt123](https://github.com/humboldt123/mutuals)

## Warning ⚠️

This project uses your discord token to scan your mutual friends list. However, never, ever, under any circumstances give your token to anybody as it would give them full access to your account. Before running this program, I highly recommend reading through the code to make sure it is something you trust.

## Requirements

- If you are not on Windows : [Python 3.9](https://www.python.org/downloads/) (or higher) and [pip](https://pip.pypa.io/en/stable/installation/) (should be installed with Python)
- A web browser

## Setup

### On windows

If you are on Windows, you can download the executable from the [latest release](https://github.com/arnaud-ma/friends-network-graph/releases/latest) and run it.


### On any OS

After installing Python, download the source code from the [latest release](https://github.com/arnaud-ma/friends-network-graph/releases/latest) and extract it.
Navigate to it with a terminal then run ```pip install -r requirements.txt``` to install its dependencies and ```python start.py``` to run it.

## Usage

Just follow the instructions displayed in the terminal.

You may be asked to give your discord token.  
⚠️BEFORE DOING ANYTHING READ THE WARNING SECTION ⚠️  
To get it, log into Discord on a browser. Open Developer Tools, then click Network. Press F5 on your keyboard to reload the page. Type /api into the Filter field, then click library. Click the Headers tab, then scroll down to authorization to find your Discord token.

## Config / customization

You can edit the ``config.py`` file in the tools folder to change several things:

- output file paths (data, html page etc.)
- The size of the nodes according to the number of connections with the``expr_size`` function
- Display or not on the page a whole bunch of editable options directly next to the graph

For the last point, you can see the documentation of all the options [here](https://visjs.github.io/vis-network/docs/network/), more particularly:

- [nodes](https://visjs.github.io/vis-network/docs/network/nodes.html)
- [edges](https://visjs.github.io/vis-network/docs/network/edges.html)
- [physics](https://visjs.github.io/vis-network/docs/network/physics.html)
- [interaction](https://visjs.github.io/vis-network/docs/network/interaction.html)
- [layout](https://visjs.github.io/vis-network/docs/network/layout.html)

## Contributing

If you want to contribute to this project, feel free to open a pull request or an issue.

If you want to add a new social media, you can create a new folder with the name of the social media in the main folder.
Then update the ``tree_input.py`` to add the new social media in the output tree.
