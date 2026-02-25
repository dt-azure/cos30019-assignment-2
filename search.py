import sys
from setup import Graph, GraphProblemMultiDest
from iterative_deepening_a_star import ida_star_search

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
            elif line == "":
                continue
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
                    goals = list(map(int, line.split("; ")))

        return graph, coords, origin, goals

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please follow this format: python search.py <filename> <method>")
        print("<filename>: name of the input file")
        print("<method>: bfs, dfs, gbfs, a_star, cus1, cus2")
    
    try:
        graph, coords, origin, goals = parse_input("sample_input.txt")
        # print(graph.nodes())
        
        # print(graph.get(2, 1))
        # print(graph.get(4, 1))
        # print(graph.get(5, 4))

        # print(coords)
        # print(origin)
        print(goals)
        problem = GraphProblemMultiDest(origin, goals, graph, coords)
        result, path, nodes_created = ida_star_search(problem)
        print(result)
        print(path)
        print(nodes_created)

    except FileNotFoundError:
        print("Input file does not exist. Please try again.")
