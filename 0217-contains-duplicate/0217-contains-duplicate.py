class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numToOccurence = defaultdict(int)
        for num in nums:
            numToOccurence[num] += 1

        for num in numToOccurence:
            if numToOccurence[num] > 1:
                return True
        
        return False