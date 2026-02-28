from setup import Node
from utils import euclidean_distance
from utils import PriorityQueue


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

