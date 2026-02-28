from utils.setup import Node

# Each point/place in the graph is analysed as a node
# Each node has a state (its ID)
# Each node has a parent (the node it came from)
# Each node has an action (the edge that was taken to reach it)
# Each node has a path cost (g(n)) - cumulative cost from origin to this node
# Each node has a depth (number of steps from origin)
class NodeCustom:
    def __init__(self, state, parent=None, action=None, path_cost=0, depth=0):
        self.state = state         
        self.parent = parent       
        self.action = action        
        self.path_cost = path_cost  
        self.depth = depth 

# Get neighbors of a node from edges
# Important for directed graphs
# Returns list of (neighbor_id, cost) tuples
def get_neighbors(node_id, edges):
    neighbors = []
    
    for (from_node, to_node), cost in edges.items():
        if from_node == node_id:
            neighbors.append((to_node, cost))
    
    # Sort by node_id for tie-breaking (lower ID first)
    neighbors.sort(key=lambda x: x[0])
    
    return neighbors

# Extract path from origin to goal by backtracking parents
def extract_path(node):
    path = []
    current = node
    
    while current is not None:
        path.append(current.state)
        current = current.parent
    
    # Reverse to get origin → goal order
    return list(reversed(path))

# Perform Iterative Deepening Depth-First Search (IDDFS)
def iddfs(nodes, edges, origin, destinations, track=False, visualise=False):
    # Initialise steps list for visualisation
    steps = [] if visualise else None
    
    # Check if origin is already a goal
    if origin in destinations:
        return (origin, 1, [origin])
    
    # Total nodes created across all iterations (for return value)
    total_nodes_created = 0
    # Total nodes expanded across all iterations (for visualisation display)
    total_nodes_expanded = 0
    
    # Maximum depth limit to try
    max_depth = len(nodes) 
    
    for depth_limit in range(max_depth):
        if track:
            print("\n=== Depth Limit: " + str(depth_limit) + " ===")
        
        # Perform depth-limited DFS
        result, nodes_created, nodes_expanded = depth_limited_dfs(
            nodes, edges, origin, destinations, depth_limit, track, visualise, steps, total_nodes_expanded
        )
        
        total_nodes_created += nodes_created
        total_nodes_expanded += nodes_expanded
        
        # If solution found, return it
        if result is not None:
            goal, path = result
            return (goal, total_nodes_created, path)
    
        # If cannot find solution at this depth limit
    return (None, total_nodes_created, [])

# Depth-Limited DFS helper function
def depth_limited_dfs(nodes, edges, origin, destinations, depth_limit, track=False, visualise=False, steps=None, cumulative_count=0):
    
    # Initialise stack with origin node
    origin_node = NodeCustom(state=origin, parent=None, action=None, path_cost=0, depth=0)
    stack = [origin_node]
    nodes_created = 1  # Count origin node as created
    nodes_expanded = 0
    
    while stack:
        
        # Pop from stack (LIFO - most recently added node)
        current_node = stack.pop()
        
        # Count when expanding (popping from stack)
        nodes_expanded += 1
        
        # Extract current path
        path = extract_path(current_node)
        
        if track:
            print("  [" + str(nodes_expanded) + "] Expanding node " + str(current_node.state) + " (depth=" + str(current_node.depth) + ")")
        
        # Goal test when expanding node
        if current_node.state in destinations:
            return ((current_node.state, path), nodes_created, nodes_expanded)
        
        # Check if we've reached the depth limit for this node
        if current_node.depth >= depth_limit:
            continue
        
        # Get the current branch (path from root to current node)
        branch = set()
        temp = current_node.parent
        while temp is not None:
            branch.add(temp.state)
            temp = temp.parent
        
        # Get neighbors in sorted order (for tie-breaking)
        neighbors = get_neighbors(current_node.state, edges)
        
        children_added = [] if visualise else None
        
        # Add neighbors to stack (in reverse order for correct exploration)
        for neighbor_id, edge_cost in reversed(neighbors):
            
            # Skip if neighbor is already in current branch (cycle prevention)
            if neighbor_id in branch:
                continue
            
            # Create child node
            child_node = NodeCustom(
                state=neighbor_id,
                parent=current_node,
                action=(current_node.state, neighbor_id),
                path_cost=current_node.path_cost + edge_cost,
                depth=current_node.depth + 1
            )
            
            # Add to stack for later exploration (if within depth limit)
            stack.append(child_node)
            # Count node as created when added to frontier
            nodes_created += 1

    # No solution found at this depth limit
    return (None, nodes_created, nodes_expanded)

# Implementation using Problem, original structure is kept as much as possible
def iddfs_2(problem):
    total_nodes_created = 0
    max_depth = len(problem.graph.nodes())

    for depth_limit in range(max_depth):
        result, nodes_created, _ = depth_limited_dfs_2(problem, depth_limit)

        total_nodes_created += nodes_created

        if result is not None:
            path = []
            temp = result
            while temp:
                path.append(temp.state)
                temp = temp.parent
            return result, path[::-1], total_nodes_created

    return None, None, Node.nodes_created

def depth_limited_dfs_2(problem, depth_limit):
    origin_node = Node(problem.initial)
    stack = [origin_node]

    nodes_created = 1
    nodes_expanded = 0

    while stack:
        current_node = stack.pop()
        nodes_expanded += 1

        if problem.goal_test(current_node.state):
            return current_node, nodes_created, nodes_expanded

        if current_node.depth >= depth_limit:
            continue

        branch = set()
        temp = current_node.parent
        while temp is not None:
            branch.add(temp.state)
            temp = temp.parent

        for child in reversed(current_node.expand(problem)):
            if child.state not in branch:
                stack.append(child)
                nodes_created += 1

    return None, nodes_created, nodes_expanded


