class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        minHeap = [(0, 0, 0)] #(t, r, c)

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) == (rows - 1, cols - 1):
                return t

            visit.add((0,0))
            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in nei:
                if nr not in range(rows) or nc not in range(cols) or (nr, nc) in visit:
                    continue

                wait = 0
                if abs(grid[nr][nc] - t) % 2 == 0:
                    wait = 1
                nTime = max(grid[nr][nc] + wait, t + 1)

                heapq.heappush(minHeap, (nTime, nr, nc))
                visit.add((nr,nc))

        
                    

            
            