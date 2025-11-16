class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        lastModified = -1
        lenZerosFront = 0
        lenTwosEnd = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                lastModified = lenZerosFront
                lenZerosFront += 1
            elif nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                lastModified = lenTwosEnd
                lenTwosEnd += 1
            else:
                lastModified = i
            
            if i == lastModified:
                i += 1