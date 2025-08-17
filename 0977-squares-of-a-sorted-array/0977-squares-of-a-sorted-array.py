class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        for i in range(len(nums)):
            squared.append(nums[i]**2)
        
        result = []
        left = 0
        right = len(squared) - 1
        while left < right:
            if squared[right] > squared[left]:
                result.insert(0, squared[right])
                right -= 1
            else:
                result.insert(0, squared[left])
                left += 1
            
        if left == right:
            result.insert(0, squared[left])

        return result