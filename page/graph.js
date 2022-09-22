var container = document.getElementById("network");
import connections from "../data/data.json" assert { type: "json" };
import options from "../options.json" assert { type: "json" };



console.log(typeof(connections));

var data = {nodes: [], edges: []};
var links = new Set();

// Loop through connections...

for (let id in connections) {
  let friend = connections[id];
  let n_connections = friend.connections.length;
  if (n_connections >= 0) {
    // Add to nodes
      data.nodes.push({
        id: parseInt(id),
        image: "../data/avatars/" + id + ".png",
        label: friend.username,
        size : 10*Math.sqrt(n_connections + 2),
    });
    // Add the links to our set
    friend.connections.forEach(mutual => links.add([id, mutual].sort((a, b) => parseInt(a) - parseInt(b)).join(" ")));
  }
}

// Register each link in edges
[...links].forEach(link => data.edges.push({from:parseInt(link.split(" ")[0]), to:parseInt(link.split(" ")[1])}));

var network = new vis.Network(container, data, options);