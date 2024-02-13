from collections import defaultdict

def bfs(adj, start):
    """
    Perform Breadth First Search (BFS) on the graph starting from the given node.

    Args:
    - adj (dict): The adjacency list representation of the graph.
    - start (int): The starting node for BFS.

    Returns:
    - set: Set of reachable nodes from the starting node.
    """
    visited = set()  # Set to store visited nodes
    queue = [start]  # Queue for BFS starting with the start node
    visited.add(start)  # Mark start node as visited

    while queue:
        node = queue.pop(0)  # Dequeue a node from the queue
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark neighbor as visited
                queue.append(neighbor)  # Enqueue neighbor for further exploration
    return visited

def find_reachable_nodes(arr):
    """
    Find reachable nodes for each node in the graph.

    Args:
    - arr (list): List of edges in the graph.

    Returns:
    - dict: Dictionary mapping each node to its reachable nodes.
    """
    graph = create_graph(arr)
    reachable_nodes_dict = {}
    for u in graph:
        reachable_nodes_dict[u] = bfs(graph, u)  # Perform BFS from each node to find reachable nodes

    return reachable_nodes_dict


def create_graph(arr, isDirected = True):
    graph = defaultdict(list)  # Create an empty adjacency list
    for a, b in arr:
        graph[a].append(b)  # Add edge from a to b
        if not isDirected:
            graph[b].append(a)  # Add edge from b to a
    print(graph)
    return graph


def find_node_reachable_from_all_other_nodes(reachable_nodes_dict):
    """
    Find a node that can be reached from every other node.

    Args:
    - reachable_nodes_dict (dict): Dictionary mapping nodes to their reachable nodes.

    Returns:
    - int: Node that can be reached from every other node, or -1 if no such node exists.
    """
    for node in reachable_nodes_dict:
        # Check if the current node is reachable from every other node except itself
        if all(node in reachable_nodes_dict[v] for v in reachable_nodes_dict if v != node):
            return node  # Return the node if it satisfies the condition
    return -1  # Return -1 if no such node exists


# if we want to return all nodes reachble from every node in the graph
def find_nodes_reachable_from_all_other_nodes(reachable_nodes_dict):
    """
    Find all nodes that can be reached from every other node in the graph.

    Args:
    - reachable_nodes_dict (dict): Dictionary mapping nodes to their reachable nodes.

    Returns:
    - list: List of nodes that can be reached from every other node.
    """
    # Initialize a set with all nodes in the graph
    all_nodes = set(reachable_nodes_dict.keys())

    # Initialize an empty set to store nodes that can be reached from every other node
    reachable_from_all = set()

    for node in reachable_nodes_dict:
        # Check if the current node is reachable from every other node
        if all(node in reachable_nodes_dict[v] for v in all_nodes if v != node):
            reachable_from_all.add(node)  # Add the node to the set

    return list(reachable_from_all)


# Driver code
if __name__ == '__main__':
    arr = [[1, 2], [2, 3], [4, 2], [3,1]]  # List of edges in the graph
    reachable_nodes_dict = find_reachable_nodes(arr)
    print(find_nodes_reachable_from_all_other_nodes(reachable_nodes_dict))


