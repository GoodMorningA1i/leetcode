class Solution {
    func orangesRotting(_ grid: [[Int]]) -> Int {
        var grid = grid
        var q: Deque<(Int, Int)> = []
        var time = 0
        var numFresh = 0

        var rows = grid.count
        var cols = grid[0].count

        for r in 0..<rows {
            for c in 0..<cols {
                if grid[r][c] == 1 {
                    numFresh += 1
                } else if grid[r][c] == 2 {
                    q.append((r,c))
                }
            }
        }

        var directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while !q.isEmpty && numFresh > 0 {
            var initialQLen = q.count
            for _ in 0..<initialQLen {
                var (r,c) = q.popFirst()!
                for direction in directions {
                    let dr = direction[0]
                    let dc = direction[1]
                    let updatedRow = r + dr
                    let updatedColumn = c + dc
                    if updatedRow < 0 || updatedRow == rows || updatedColumn < 0 || updatedColumn == cols || grid[updatedRow][updatedColumn] != 1 {
                        continue
                    }
                    grid[updatedRow][updatedColumn] = 2
                    q.append((updatedRow, updatedColumn))
                    numFresh -= 1
                }
            }
            time += 1
        }

        return numFresh == 0 ? time : -1
    }
}

"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Minimum grid length 1

Whenever fresh orange, we can do a check on all 4 sides to see if there is a rotten fresh. Otherwise, we can return -1
If there are no fresh oranges, then we can immediately return 0
Go through all rotten oranges and increment in one of 4 directions if possible, adjusting the grid in place, and keeping track of time (groups of oranges scattered)
Time Algorithm: O(nxm), t being the number of minutes
Space Complexity: O()
"""
