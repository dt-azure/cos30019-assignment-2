from search import parse_input
from setup import Graph, GraphProblemMultiDest
from uninformed_search import bfs, dfs
from informed_search import a_star_search, gbfs
from iterative_deepening_a_star import ida_star_search
from iterative_deepening_dfs import iddfs_2

search_algos = {
        "bfs": "Breadth First Search", 
        "dfs": "Depth First Search",
        "gbfs": "Greedy Best First Search",
        "a_star": "A* (A-star)",
        "cus1": "Custom 1",
        "ida_star": "Iterative Deepening A*"
    }

def test_algos(path):
    try:
        graph, coords, origin, goals = parse_input(f"test_cases/{path}.txt")
    except FileNotFoundError:
        print("Input file does not exist. Please try again.")
        return

    problem = GraphProblemMultiDest(origin, goals, graph, coords)

    result, result_path, nodes_created = bfs(problem)
    print(f"{path} BFS")
    print(f"{result if result else "No solution found"} {nodes_created}")
    print(f"{result_path if result_path else [ ]}")
    print("___________________")

    result, result_path, nodes_created = dfs(problem)
    print(f"{path} DFS")
    print(f"{result if result else "No solution found"} {nodes_created}")
    print(f"{result_path if result_path else [ ]}")
    print("___________________")

    result, result_path, nodes_created = gbfs(problem)
    print(f"{path} GBFS")
    print(f"{result if result else "No solution found"} {nodes_created}")
    print(f"{result_path if result_path else [ ]}")
    print("___________________")

    result, result_path, nodes_created = a_star_search(problem)
    print(f"{path} A*")
    print(f"{result if result else "No solution found"} {nodes_created}")
    print(f"{result_path if result_path else [ ]}")
    print("___________________")

    result, result_path, nodes_created = iddfs_2(problem)
    print(f"{path} IDDFS")
    print(f"{result if result else "No solution found"} {nodes_created}")
    print(f"{result_path if result_path else [ ]}")
    print("___________________")

    result, result_path, nodes_created = ida_star_search(problem)
    print(f"{path} IDA*")
    print(f"{result if result else "No solution found"} {nodes_created}")
    print(f"{result_path if result_path else [ ]}")
    print("___________________")

if __name__ == "__main__":
    while True:
        path = input("Enter test case name: ")

        if path == "exit":
            exit()
        else:
            test_algos(path)
            print("\n")
            print ("\n")



