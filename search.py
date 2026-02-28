import sys
from setup import Graph, GraphProblemMultiDest
from iterative_deepening_a_star import ida_star_search
from uninformed_search import bfs, dfs
from informed_search import a_star_search, gbfs
from iterative_deepening_dfs import iddfs_2

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
    search_algos = {
        "bfs": "Breadth First Search", 
        "dfs": "Depth First Search",
        "gbfs": "Greedy Best First Search",
        "a_star": "A* (A-star)",
        "iddfs": "Iterarive Deepening Depth First Search",
        "ida_star": "Iterative Deepening A*"
    }

    if len(sys.argv) != 3:
        print("Please follow this format: python search.py <filename> <method>")
        print("<filename>: name of the input file (without extension). Input file must be a txt file and must be inside the test_cases folder.")
        print("<method>: bfs, dfs, gbfs, a_star, iddfs, ida_star")
        print("Example: python search.py test_case_1 bfs")
        exit()

    _, path, search_algo = sys.argv

    if search_algo not in search_algos.keys():
        print("Invalid search algorithm. Please choose one from this list: bfs, dfs, gbfs, a_star, cus1, ida_star.")
        exit()

    try:
        graph, coords, origin, goals = parse_input(f"test_cases/{path}.txt")
    except FileNotFoundError:
        print("Input file does not exist. Please try again.")
        exit()

    problem = GraphProblemMultiDest(origin, goals, graph, coords)

    if search_algo == "bfs":
        result, result_path, nodes_created = bfs(problem)
    elif search_algo == "dfs":
        result, result_path, nodes_created = dfs(problem)
    elif search_algo == "gbfs":
        result, result_path, nodes_created = gbfs(problem)
    elif search_algo == "a_star":
        result, result_path, nodes_created = a_star_search(problem)
    elif search_algo == "iddfs":
        result, result_path, nodes_created = iddfs_2(problem)
    elif search_algo == "ida_star":
        result, result_path, nodes_created = ida_star_search(problem)

    print(f"{path} {search_algos[search_algo]}")
    print(f"{result if result else "No solution found"} {nodes_created}")
    print(f"{result_path if result_path else [ ]}")
