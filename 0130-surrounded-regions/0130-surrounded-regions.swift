class Solution {
    func solve(_ board: inout [[Character]]) {

        let rows = board.count
        let cols = board[0].count

        func capture(_ r: Int, _ c: Int) {
            if r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != "O" {
                return
            }
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        }

        //Turn all unsurrounded regions into T
        for r in 0..<rows {
            for c in 0..<cols {
                if board[r][c] == "O" && r == 0 || r == rows - 1 || c == 0 || c == cols - 1 {
                    capture(r,c)
                }
            }
        }

        //Turn all surrounded regions into X
        for r in 0..<rows {
            for c in 0..<cols {
                if board[r][c] == "O" {
                    board[r][c] = "X"
                }
            }
        }

        //Turn all T back into O
        for r in 0..<rows {
            for c in 0..<cols {
                if board[r][c] == "T" {
                    board[r][c] = "O"
                }
            }
        }

    }
}