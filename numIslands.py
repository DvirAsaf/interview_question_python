"""
200. Number of Islands
Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume water all surrounds all four edges of the grid.
"""
from typing import List


def num_islands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                self.dfs(grid, r, c)
                islands += 1

    return islands


def dfs(self, grid, r, c):
    grid[r][c] = '0'
    rows = len(grid)
    cols = len(grid[0])
    for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
        row = r + dr
        col = c + dc
        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == '1':
            self.dfs(grid, row, col)
