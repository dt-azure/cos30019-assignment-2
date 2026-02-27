import tracemalloc
import time
from search import parse_input
from setup import Graph, GraphProblemMultiDest
from iterative_deepening_a_star import ida_star_search
from uninformed_search import bfs, dfs
from astar_search import a_star_search
import numpy as np

def test_algo(path):
    graph, coords, origin, goals = parse_input(path)
    problem = GraphProblemMultiDest(origin, goals, graph, coords)

    # BFS
    avg = []
    current_avg = []
    peak_avg = []
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        bfs(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    print(f"BFS avg execution time: {np.mean(avg) * 1000:.3f} ms")
    print(f"BFS avg memory allocated: {np.mean(current_avg)} bytes")
    print(f"BFS avg peak memory usage: {np.mean(peak_avg)} bytes")

    avg = []
    current_avg = []
    peak_avg = []
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        dfs(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    print(f"DFS avg execution time: {np.mean(avg) * 1000:.3f} ms")
    print(f"DFS avg memory allocated: {np.mean(current_avg)} bytes")
    print(f"DFS avg peak memory usage: {np.mean(peak_avg)} bytes")

    avg = []
    current_avg = []
    peak_avg = []
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        ida_star_search(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    print(f"IDA* avg execution time: {np.mean(avg) * 1000:.3f} ms")
    print(f"IDA* avg memory allocated: {np.mean(current_avg)} bytes")
    print(f"IDA* avg peak memory usage: {np.mean(peak_avg)} bytes")

    avg = []
    current_avg = []
    peak_avg = []
    for _ in range(50):
        tracemalloc.start()

        start = time.perf_counter()
        a_star_search(problem)
        end = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg.append(end - start)
        current_avg.append(current)
        peak_avg.append(peak)

    print(f"A* avg execution time: {np.mean(avg) * 1000:.3f} ms")
    print(f"A* avg memory allocated: {np.mean(current_avg)} bytes")
    print(f"A* avg peak memory usage: {np.mean(peak_avg)} bytes")

if __name__ == "__main__":
    test_algo('test_case_5.txt')
