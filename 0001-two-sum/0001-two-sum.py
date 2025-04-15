class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}
        for i in range(0, len(nums)):
            if nums[i] not in value_to_index:
                value_to_index[nums[i]] = i
            
        print(value_to_index)
                
        for i in range(0, len(nums)):
            complacent = target - nums[i]
            if complacent in value_to_index and i != value_to_index[complacent]:
                return [i, value_to_index[complacent]]