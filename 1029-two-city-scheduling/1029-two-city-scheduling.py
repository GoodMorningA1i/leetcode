class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
            diffs.sort()
        n = len(costs) // 2 #guaranteed to be even
        for i in range(n):
            res += diffs[i][2] #city B Total
        for i in range(n, len(costs)):
            res += diffs[i][1]
        
        return res