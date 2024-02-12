"""
1971. find-if-path-exists-in-graph
There is a bidirectional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges,
where each edges[i] = [ui, vi] denotes a bidirectional edge between vertex ui and vertex vi.
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
You want to determine if there is a valid path that exists from vertex source to vertex destination.
Given edges and the integers n, source, and destination,
return true if there is a valid path from source to destination, or false otherwise.
Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""
import collections
from typing import List


def valid_path(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # Store all edges in 'graph'.
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Store all the nodes to be visited in 'queue'.
    seen = [False] * n
    seen[source] = True
    queue = collections.deque([source])

    while queue:
        curr_node = queue.popleft()
        if curr_node == destination:
            return True

        # For all the neighbors of the current node, if we haven't visit it before,
        # add it to 'queue' and mark it as visited.
        for next_node in graph[curr_node]:
            if not seen[next_node]:
                seen[next_node] = True
                queue.append(next_node)

    return False
