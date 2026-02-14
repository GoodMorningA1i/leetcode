class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        [0,1,0,3,2,3]
                   ^

        res = [0, 1, 2, 3]
                     ^
        i = 4
        nums[i] = 2
        res[-1] = 3

        """
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                j = 0
                while nums[i] > res[j]:
                    j += 1
                res[j] = nums[i]

        return len(res)