"""
118. pascals-triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]
"""
from typing import List


def generate(self, numRows: int) -> List[List[int]]:
    triangles = []
    for i in range(numRows):
        triangles.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                triangles[i].append(1)
            else:
                triangles[i].append(triangles[i - 1][j - 1] + triangles[i - 1][j])
    return triangles
