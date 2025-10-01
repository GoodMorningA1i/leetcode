from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visit = set()
        rows = len(grid)
        columns = len(grid[0])

        def bfs(row, column):
            q = deque()
            q.append((row, column))
            visit.add((row, column))

            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    updatedRow = r + dr
                    updatedColumn = c + dc
                    if updatedRow in range(rows) and updatedColumn in range(columns) and grid[updatedRow][updatedColumn] == "1" and (updatedRow, updatedColumn) not in visit:
                        q.append((updatedRow, updatedColumn))
                        visit.add((updatedRow, updatedColumn))

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in visit:
                    result += 1
                    bfs(row, column)

        return result


"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


numIslands, grid be an array of an array of strings and returns an int


[['1', '1', 1', '0', '0'],
['1', '1', 0', '0', '0'],
['1', '1', '1', '1', '0'],
['0', '0', '0', '0', '1']]'

output = 2

BFS
Time Complexity: O(m*n)
Space Complexity: O(m*n)

O(V+E)

[0,0]: [[0,1], [1,0]]

visited queue = what elements have you visited (set)
to be visited = what elements do you still need to visit (queue)


"""