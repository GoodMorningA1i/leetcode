from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        res = 0
        
        def bfs(row, column):
            area = 0
            visit.add((row,column))
            q = deque()
            q.append((row,column))

            while q:
                r,c = q.popleft()
                area += 1
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(m) and nc in range(n) and grid[nr][nc] == 1 and (nr, nc) not in visit:
                        q.append((nr,nc))
                        visit.add((nr,nc))
            return area


        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r, c)
                    res = max(area, res)
        
        return res
