class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        
        nums.sort()

        prev = 0
        for i in range(len(nums)):
            a = nums[i]
            if i != 0 and a == prev:
                continue
        
            pointerA = i + 1
            pointerB = len(nums) - 1

            while pointerA < pointerB:
                if a + nums[pointerA] + nums[pointerB] < 0:
                    pointerA += 1
                elif a + nums[pointerA] + nums[pointerB] > 0:
                    pointerB -= 1
                else:
                    triplets.append([a, nums[pointerA], nums[pointerB]])
                    pointerA += 1
                    while pointerA < pointerB and nums[pointerA] == nums[pointerA - 1]:
                        pointerA += 1
            
            prev = a

        return triplets



