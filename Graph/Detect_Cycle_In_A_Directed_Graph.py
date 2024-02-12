# """
#
#
# """
import collections
from typing import List


def detect_cycle_in_directed_graph(vertices: List[List[int]], n):
    def dfs(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                if dfs(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        rec_stack[node] = False

        return False

    graph = collections.defaultdict(list)
    for a, b in vertices:
        graph[a].append(b)

    visited = [False] * (n + 1)
    rec_stack = [False] * (n + 1)
    for node in range(n):
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True
    print(visited)
    return False


if __name__ == '__main__':
    print(detect_cycle_in_directed_graph([[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]], 4))
