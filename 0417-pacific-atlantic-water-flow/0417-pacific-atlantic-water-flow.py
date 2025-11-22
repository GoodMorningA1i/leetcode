class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])
        
        def canReachPacific(row, column):
            visited = {(row,column)}
            q = collections.deque()
            q.append((row,column))

            while q:
                r, c = q.popleft()
                visited.add((r,c))

                directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr not in range(rows) or nc not in range(cols)) and (nr == r - 1 or nc == c - 1): #At pacific border
                        return True
                    if nr in range(rows) and nc in range(cols) and heights[r][c] >= heights[nr][nc] and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr,nc))
                    
            return False

        def canReachAtlantic(row, column):
            visited = {(row,column)}
            q = collections.deque()
            q.append((row,column))

            while q:
                r, c = q.popleft()
                visited.add((r,c))

                directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr not in range(rows) or nc not in range(cols)) and (nr == r + 1 or nc == c + 1): #At atlantic border
                        return True
                    if nr in range(rows) and nc in range(cols) and heights[r][c] >= heights[nr][nc] and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr,nc))

            return False

        
        for r in range(rows):
            for c in range(cols):
                if canReachPacific(r, c) and canReachAtlantic(r,c): #BFS
                    res.append([r,c])

        return res
        
