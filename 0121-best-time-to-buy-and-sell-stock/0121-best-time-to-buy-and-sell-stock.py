class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxResult = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            maxResult = max(maxResult, prices[r] - prices[l])
            r += 1

        return maxResult

"""
prices = [5,2,5,9,1]
Buy on prices[1], sell on prices[3]
"""