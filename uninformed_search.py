from collections import deque
from setup import Node

def bfs(problem):
    Node.nodes_created = 0
    frontier = deque([Node(problem.initial)])
    visisted = set()
    visisted.add(problem.initial)

    while frontier:
        node = frontier.popleft()

        if problem.goal_test(node.state):
            result_path = []
            result = node

            while result:
                result_path.append(result.state)
                result = result.parent
            return node, result_path[::-1], Node.nodes_created
        
        for child in node.expand(problem):
            if child.state not in visisted:
                visisted.add(node.state)
                frontier.append(child)

    return None, None, Node.nodes_created

def dfs(problem):
    Node.nodes_created = 0
    frontier = [Node(problem.initial)]
    visisted = set()

    while frontier:
        node = frontier.pop()

        if problem.goal_test(node.state):
            result_path = []
            result = node

            while result:
                result_path.append(result.state)
                result = result.parent
            return node, result_path[::-1], Node.nodes_created
        
        if node.state not in visisted:
            visisted.add(node.state)
            
            for child in reversed(node.expand(problem)):
                if child.state not in visisted and child not in frontier:
                    frontier.append(child)
    
    return None, None, Node.nodes_created

    