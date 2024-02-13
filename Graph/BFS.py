from collections import defaultdict, deque

def create_graph(arr_1, arr_2):
    graph = defaultdict(list)
    for i in range(len(arr_1)):
        graph[arr_1[i]].append(arr_2[i])
        graph[arr_2[i]].append(arr_1[i])
    return graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


if __name__ == '__main__':
    # Example usage:
    arr_1 = [1, 2, 3, 4, 5]
    arr_2 = [2, 3, 4, 5, 1]

    graph = create_graph(arr_1, arr_2)
    print("Graph:", graph)

    start_node = arr_1[0]  # Starting from the first node in arr_1
    print("BFS traversal from node", start_node, ":")
    bfs(graph, start_node)
