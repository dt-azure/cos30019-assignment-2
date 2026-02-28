from utils.setup import Node
from utils.utils import euclidean_distance, PriorityQueue
import heapq
import math


def a_star_search(problem):
    """
    A* search implementation
    f(n) = g(n) + h(n)
    """
    frontier = PriorityQueue('min', f=lambda n: (n.path_cost + problem.h(n), n.state))
    
    Node.nodes_created = 0
    
 
    root = Node(problem.initial)
    frontier.append(root)
    

    reached = {problem.initial: root}

    while frontier:
        node = frontier.pop()

        if problem.goal_test(node.state):
            result_path = []
            current = node
            while current is not None:
                result_path.append(current.state)
                current = current.parent
            result_path.reverse()
            return node, result_path, Node.nodes_created

        for action in problem.actions(node.state):
            child = node.child_node(problem, action)
            s = child.state
            
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.append(child)

    return None, None, Node.nodes_created

def gbfs(problem):

    Node.nodes_created = 0
    start = Node(problem.initial)

    frontier = []
    insertion_order = 0

    def push(node):
        nonlocal insertion_order
        heapq.heappush(
            frontier,
            (problem.h(node), node.state, insertion_order, node)
        )
        insertion_order += 1

    push(start)

    explored = set()
    frontier_states = {start.state}

    while frontier:
        _, _, _, node = heapq.heappop(frontier)
        frontier_states.remove(node.state)

        if problem.goal_test(node.state):
            result_path = []
            result = node

            while node:
                result_path.append(node.state)
                node = node.parent
            return result, result_path[::-1], Node.nodes_created

        explored.add(node.state)

        children = node.expand(problem)
        children.sort(key=lambda n: n.state)

        for child in children:
            if child.state not in explored and child.state not in frontier_states:
                push(child)
                frontier_states.add(child.state)

    return None, None, Node.nodes_created

def ida_star_search(problem):
    root = Node(problem.initial)

    # Threshold: f(n) = g(n) + h(n)
    # g(root) = 0
    threshold = problem.h(root)

    # Recursive DFS, when f(n) exceeds threshold that branch is pruned
    def search(node, threshold, path):
        f = node.path_cost + problem.h(node)

        if f > threshold:
            return f
        
        if problem.goal_test(node.state):
            return node
        
        minimum = math.inf
        path.add(node.state)

        for child in node.expand(problem):
            if child.state not in path:
                result = search(child, threshold, path)

                if isinstance(result, Node):
                    return result
                
                minimum = min(minimum, result)
        
        path.remove(node.state)
        return minimum

    while True:
        Node.nodes_created = 0
        path = set()
        result = search(root, threshold, path)

        if isinstance(result, Node):
            result_path = []
            node = result

            # Tracing back from the final node to the original node
            while node:
                result_path.append(node.state)
                node = node.parent

            return result, result_path[::-1], Node.nodes_created
        
        # If result is inf -> no solution exists
        if result == math.inf:
            return None, None, Node.nodes_created
        
        # Else increase threshold to the smallest f(n) that exceeds threshold
        threshold = result