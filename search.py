import sys
from utils.setup import Graph, GraphProblemMultiDest, parse_input
from algorithms.uninformed_search import bfs, dfs, iddfs_2
from algorithms.informed_search import a_star_search, gbfs, ida_star_search

search_algos = {
        "bfs": "Breadth First Search", 
        "dfs": "Depth First Search",
        "gbfs": "Greedy Best First Search",
        "a_star": "A* (A-star)",
        "iddfs": "Iterarive Deepening Depth First Search",
        "ida_star": "Iterative Deepening A*"
    }

def program():
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

if __name__ == "__main__":  
    program()
