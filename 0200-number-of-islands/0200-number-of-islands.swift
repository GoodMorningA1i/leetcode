class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        let rows = grid.count
        let cols = grid[0].count
        var visited: Set<[Int]> = Set()
        var numIslands = 0

        func bfs(_ r: Int, _ c: Int) {
            var q: Deque<(Int, Int)> = []
            q.append((r,c))
            visited.insert([r,c])
            while !q.isEmpty {
                let (row, column) = q.popFirst()!
                let directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for (dr, dc) in directions {
                    let nr = row + dr, nc = column + dc
                    if nr >= 0, nr < rows, nc >= 0, nc < cols, grid[nr][nc] == "1", !visited.contains([nr,nc]) {
                        q.append((nr, nc))
                        visited.insert([nr,nc])
                    }
                }
            }
        }

        for r in 0..<rows {
            for c in 0..<cols {
                if grid[r][c] == "1", !visited.contains([r,c]) {
                    bfs(r, c)
                    numIslands += 1
                }
            }
        }

        return numIslands
    }
}
