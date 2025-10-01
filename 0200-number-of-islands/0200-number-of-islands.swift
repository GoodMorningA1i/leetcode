class Solution {
    func numIslands(_ grid: [[Character]]) -> Int {
        var result = 0
        var visited = Set<[Int]>()
        let rows = grid.count
        let cols = grid[0].count

        func bfs(_ row: Int, _ col: Int) {
            var queue: [[Int]] = [[row, col]]
            visited.insert([row, col])
            
            while !queue.isEmpty {
                let current = queue.removeFirst()
                let r = current[0], c = current[1]
                
                let directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dir in directions {
                    let newRow = r + dir[0]
                    let newCol = c + dir[1]
                    
                    if newRow >= 0, newRow < rows,
                       newCol >= 0, newCol < cols,
                       grid[newRow][newCol] == "1",
                       !visited.contains([newRow, newCol]) {
                        
                        queue.append([newRow, newCol])
                        visited.insert([newRow, newCol])
                    }
                }
            }
        }
        
        for row in 0..<rows {
            for col in 0..<cols {
                if grid[row][col] == "1", !visited.contains([row, col]) {
                    result += 1
                    bfs(row, col)
                }
            }
        }
        
        return result
    }
}