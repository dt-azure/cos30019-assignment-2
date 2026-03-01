import tracemalloc
import time
from utils.setup import parse_input, GraphProblemMultiDest
from algorithms.uninformed_search import bfs, dfs, iddfs_2
from algorithms.informed_search import a_star_search, gbfs, ida_star_search
import numpy as np
import sys

def print_results(algo, avg, current_avg, peak_avg, nodes_created):
    print(f"{algo} avg execution time: {np.mean(avg) * 1000:.3f} ms")
    print(f"{algo} avg memory allocated: {np.mean(current_avg)} bytes")
    print(f"{algo} avg peak memory usage: {np.mean(peak_avg)} bytes")
    print(f"{algo} nodes created: {nodes_created}")

def print_results_bare(algo, avg, current_avg, peak_avg, nodes_created):
    avg = round(np.mean(avg) * 1000, 3)
    current_avg = np.mean(current_avg)
    peak_avg = np.mean(peak_avg)

    print(f"{algo} - {avg}, {current_avg}, {peak_avg}, {nodes_created}")


def test_algo(path, clean_output = True):
    graph, coords, origin, goals = parse_input(path)
    problem = GraphProblemMultiDest(origin, goals, graph, coords)

    # BFS
    avg = []
    current_avg = []
    peak_avg = []
    nodes_created = 0
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        _, _, nodes_created = bfs(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    if clean_output:
        print_results("BFS", avg, current_avg, peak_avg, nodes_created)
    else:
        print_results_bare("BFS", avg, current_avg, peak_avg, nodes_created)

    avg = []
    current_avg = []
    peak_avg = []
    nodes_created = 0
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        _, _, nodes_created = dfs(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    if clean_output:
        print_results("BFS", avg, current_avg, peak_avg, nodes_created)
    else:
        print_results_bare("DFS", avg, current_avg, peak_avg, nodes_created)

    avg = []
    current_avg = []
    peak_avg = []
    nodes_created = 0
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        _, _, nodes_created = gbfs(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    if clean_output:
        print_results("GBFS", avg, current_avg, peak_avg, nodes_created)
    else:
        print_results_bare("GBFS", avg, current_avg, peak_avg, nodes_created)

    avg = []
    current_avg = []
    peak_avg = []
    nodes_created = 0
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        _, _, nodes_created = a_star_search(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    if clean_output:
        print_results("A*", avg, current_avg, peak_avg, nodes_created)
    else:
        print_results_bare("A*", avg, current_avg, peak_avg, nodes_created)

    avg = []
    current_avg = []
    peak_avg = []
    nodes_created = 0
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        _, _, nodes_created = iddfs_2(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    if clean_output:
        print_results("IDDFS", avg, current_avg, peak_avg, nodes_created)
    else:
        print_results_bare("IDDFS", avg, current_avg, peak_avg, nodes_created)

    avg = []
    current_avg = []
    peak_avg = []
    nodes_created = 0
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        _, _, nodes_created = ida_star_search(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    if clean_output:
        print_results("IDA*", avg, current_avg, peak_avg, nodes_created)
    else:
        print_results_bare("IDA*", avg, current_avg, peak_avg, nodes_created)

if __name__ == "__main__":
    _, path, clean_output = sys.argv
    clean_output = True if clean_output == 1 else False

    test_algo(f"test_cases/{path}.txt", clean_output)
