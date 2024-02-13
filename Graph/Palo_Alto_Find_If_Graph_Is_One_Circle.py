"""
Given 2 arrays representing a graph, return True if the following requirement is existing:
1. all nodes in the graph are connected
2. all nodes are one big circle.
 example:
 input: arr_1 = [1,2,3]     arr_2 = [2,3,1]
 output: True
 explained: arr_1[0] == 1  connected to arr_2[0] == 2 meaning node 1 connected to mode 2          1
          arr_1[1] == 2  connected to arr_2[1] == 3 meaning node 2 connected to mode 3          /  \
          arr_1[2] == 1  connected to arr_2[2] == 1 meaning node 3 connected to mode 1         3 _ 2
*** all nodes are bidirectional meaning that if node 1 connected to mode 2 also, meaning node 2 connected to mode 1.
"""
import collections


def is_one_big_circle(arr_1, arr_2):

    n = len(arr_1)
    # Constructing the graph
    graph = collections.defaultdict(list)
    for a, b in zip(arr_1, arr_2):
        graph[a].append(b)
        graph[b].append(a)

    # Checking if all nodes are connected
    visited = {node: False for node in graph}
    stack = [arr_1[0]]
    visited[arr_1[0]] = True

    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    if not all(visited.values()):
        return False

    # Checking if all nodes form a single circle
    for node in graph:
        if len(graph[node]) != 2:
            return False

    return True


if __name__ == '__main__':
    arr1 = [1, 1]
    arr2 = [2, 3]
    print(is_one_big_circle(arr1, arr2))
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [2, 3, 4, 6, 1, 5]
    print(is_one_big_circle(arr1, arr2))
    arr1 = [1]
    arr2 = [2]
    print(is_one_big_circle(arr1, arr2))
    arr1 = [1,3]
    arr2 = [2,4]
    print(is_one_big_circle(arr1, arr2))
    arr1 = [1,2,3]
    arr2 = [2,3,1]
    print(is_one_big_circle(arr1, arr2))
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 1, 5, 4]
    print(is_one_big_circle(arr1, arr2))
    arr1 = [1, 2, 3, 4]
    arr2 = [2, 3, 1, 5]
    print(is_one_big_circle(arr1, arr2))
    arr1 = [1, 2, 3, 4]
    arr2 = [2, 3, 4, 1]
    print(is_one_big_circle(arr1, arr2))

