from setup import Node
import math


def ida_star_search(problem):
    root = Node(problem.initial)
    threshold = problem.h(root)

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

            while node:
                result_path.append(node.state)
                node = node.parent

            return result, result_path[::-1], Node.nodes_created
        
        if result == math.inf:
            return None, None, Node.nodes_created
        
        threshold = result
