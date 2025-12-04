"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

[
[0, 1, 1,0,1,0]
[0, 1, 1,1,0,0]
[0, 1, 1,0,0,0]
[0, 1, 0,0,0,0]
[0, 1, 1,1,1,0]
]

max = 12

1 <= m, n <= 50
grid only contains 1, 0
multiple islands in the graph

O(MxN)
O(MxN)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Iterate through this graph/grid
        When we reach a 1, we need to check the area of that island (graph traversal algorithm)
        - BFS (we start when we reach a element that is 1)
        - We add the node currently being processed to the visited set
        - From this 1, we have to check the 4 directions (up, right, left, down)
        - We add those neighbours only if there are 1 to the To be visited queue
        Repeat
        """
        visited = set()
        rows = len(grid)
        columns = len(grid[0])
        maxArea = 0
        
        def bfs(row, column) -> int:
            toBeVisited = deque()
            toBeVisited.append((row, column))
            visited.add((row,column)) #need to do this at the same time
            count = 0 
            
            while toBeVisited:
                r, c = toBeVisited.popleft()
                count += 1
                directions = [[0, 1], [0, -1], [1, 0], [-1,0]]
                for dr, dc in directions:
                    updatedRow = r + dr
                    updatedColumn = c + dc
                    if updatedRow in range(rows) and updatedColumn in range(columns) and grid[updatedRow][updatedColumn] == 1 and (updatedRow, updatedColumn) not in visited:
                        toBeVisited.append((updatedRow, updatedColumn))
                        visited.add((updatedRow, updatedColumn)) #forgot this line
                        
            return count
            
        
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
            
        return maxArea

    """
    [[1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]]

    visited = ((0,0), (0,1), (1,0))
    toBeVisited = queue[(1,1)]
    count = 3

    """


"""
[
[0, 1, 1,0,1,0]
[0, 1, 1,1,0,0]
[0, 1, 1,0,0,0]
[0, 1, 0,0,0,0]
[0, 1, 1,1,1,0]
]

visited = ((0,1))
toBeVisited = queue[(0,2), (1,1)]
count = 3
maxArea = 12
"""