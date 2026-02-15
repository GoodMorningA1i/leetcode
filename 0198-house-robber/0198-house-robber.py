class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp = [2,1,3,3]

        """


        dp = [0] * len(nums)
        dp[0] = nums[0]

        if len(nums) > 1:
            dp[1] = nums[1]
        
        for i in range(2, len(nums)):
            for j in range(0, i - 1):
                temp = nums[i] + dp[j]
                dp[i] = max(dp[i], temp)

        return max(dp)