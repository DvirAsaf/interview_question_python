"""
207. course-schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi
first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
import collections
from typing import List


def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    def dfs(node, graph, visited, rec_stack):
        if rec_stack[node]:
            return True
        if visited[node]:
            return False
        visited[node] = True
        rec_stack[node] = True
        for neighbour in graph[node]:
            if dfs(neighbour, graph, visited, rec_stack):
                return True

        rec_stack[node] = False
        return False

    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    visited = [False] * (numCourses)
    rec_stack = [False] * (numCourses)
    for node in range(numCourses):
        if dfs(node, graph, visited, rec_stack):
            return False

    return True
