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
    def isCyclicUtil( v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in graph[v]:
            if visited[neighbour] == False:
                if isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[v] = False
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
from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


# if __name__ == '__main__':
#     g = Graph(4)
#     g.addEdge(0, 1)
#     g.addEdge(0, 2)
#     g.addEdge(1, 2)
#     g.addEdge(2, 0)
#     g.addEdge(2, 3)
#     g.addEdge(3, 2)
#     if g.isCyclic() == 1:
#         print("Graph contains cycle")
#     else:
#         print("Graph doesn't contain cycle")
