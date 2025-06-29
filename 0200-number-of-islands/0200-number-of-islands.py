class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visit = set()
        rows = len(grid)
        columns = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row, column = q.popleft()
                directions = [[0,1], [0,-1], [-1,0], [1,0]]
                for dr, dc in directions:
                    r,c = row + dr, column + dc
                    if r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(0, rows):
            for c in range(0, columns):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands
                

                
