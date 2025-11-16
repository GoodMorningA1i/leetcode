class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for j in range(len(matrix[0])):
            curr = []
            for i in range(len(matrix)):
                curr.append(matrix[i][j])
            res.append(curr)
        return res