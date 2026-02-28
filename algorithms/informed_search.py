from utils.setup import Node
from utils.utils import euclidean_distance, PriorityQueue
import heapq


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