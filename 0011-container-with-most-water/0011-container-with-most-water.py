class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = min(height[r], height[l]) * (r - l)
            res = max(res, area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        return res
