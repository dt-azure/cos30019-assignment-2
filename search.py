import sys

class Graph:
    """A graph connects nodes (vertices) by edges (links). Each edge can also
    have a length associated with it. The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C. You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more links with g.connect('B', 'C', 3), then
    inverse link is also added. You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B. 'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


def UndirectedGraph(graph_dict=None):
    """Build a Graph where every edge (including future ones) goes both ways."""
    return Graph(graph_dict=graph_dict, directed=False)

def parse_input(path):
    flag = None
    graph = Graph()
    coords = {}
    origin = None
    goals = set()

    with open(path) as input_file:
        for line in input_file:
            line = line.strip()

            if line == "Nodes:":
                flag = "nodes"
            elif line == "Edges:":
                flag = "edges"
            elif line == "Origin:":
                flag = "origin"
            elif line == "Destinations:":
                flag = "dests"
            else:
                if flag == "nodes":
                    node, node_coords = line.split(": ")
                    x, y = map(int, node_coords[1:-1].split(","))
                    coords[int(node)] = (x, y)
                elif flag == "edges":
                    nodes, cost = line.split(": ")
                    start, end = map(int, nodes[1:-1].split(","))
                    graph.connect(start, end, int(cost))
                elif flag == "origin":
                    origin = int(line)
                elif flag == "dests":
                    goals = set(map(int, line.split("; ")))

        return graph, coords, origin, goals



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please follow this format: python search.py <filename> <method>")
        print("<filename>: name of the input file")
        print("<method>: bfs, dfs, gbfs, a_star, cus1, beam_search")
    
    try:
        graph, coords, origin, goals = parse_input("sample_input.txt")
        print(graph.nodes())
        
        print(graph.get(2, 1))
        print(graph.get(4, 1))
        print(graph.get(5, 4))

        print(coords)
        print(origin)
        print(goals)
    except FileNotFoundError:
        print("Input file does not exist. Please try again.")
