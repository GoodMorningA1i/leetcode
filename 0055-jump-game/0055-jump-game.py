class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """

        """


        i = len(nums) - 1 - 1
        flag = len(nums) - 1
        
        while i >= 0:
            if flag - i <= nums[i]:
                flag = i
            i -= 1

        return flag == 0
            