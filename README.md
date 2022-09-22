
# Social-network-graph

 Create a network graph of your friends on a social media.  
 Inspired by [humboldt123](https://github.com/humboldt123/mutuals)

## Requirements

- Python 3.10+ with pip (you can download it [here](https://www.python.org/downloads/))
- A web browser

## Setup

After installing Python, download this repository [here](https://github.com/arnaud-ma/friends-network-graph/archive/refs/heads/main.zip) or clone it.  

Navigate to it with a terminal then run ```pip -r requirements.txt``` to install its dependencies and ```py start.py``` to run it.

Follow the instructions displayed in the terminal. Creating the graph can take several tens of seconds so please wait when a blank page appears.

## Personalization

You can personalize the graph by editing the ```options.json``` file. You can find all possible customizations in the documentation [here](https://visjs.github.io/vis-network/docs/network/#options).  
For example if nodes fidget too much, you can decrease the value of ```springConstant```

For even more customization, it is possible to modify the file ```graph.js``` at the twentieth line.  
For example if nodes are too small or big, you can change the ```size``` argument (or even delete it).
