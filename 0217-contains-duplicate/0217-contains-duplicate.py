class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False

        #Brute force
        #Go through the entire array
        #Create a dictionary with each of the elements
        #If any of the dictionary values is greater than 1, than true
        #Time Complexity: O(n + n) = O(2n) = O(n)
        #Space Complexity: O(n)

        #Optimize
        #Binary sort
        #Time Complexity: O(n) = O(nlogn + n)
        #Space Complexity: O(1)

