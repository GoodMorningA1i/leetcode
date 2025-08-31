class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        result = 0
        l_near = 0
        l_far = 0

        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[l_near]] -= 1
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                l_near += 1
                l_far = l_near
            
            while count[nums[l_near]] > 1:
                count[nums[l_near]] -= 1
                l_near += 1
                #move l_near by one

            if len(count) == k:
                result += l_near - l_far + 1

        return result