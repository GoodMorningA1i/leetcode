class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [4,5,6,7,0,1,2]

        When I think about solving this in O(logn), I think about how can I get rid of half
        of the things I need to look at, at each iteration. 
        Right now, my only idea is splitting the array in half.
        Well, we do know we can get rid at most half of the values in the list. We just don't 
        what the positions are.

        But we do know this is an ascending order, just left rotated from k
        Can we identify the k somehow?


        [4,5,6,7,0,1,2]
               ^
        --------|
                |------

        target = 0
        At 7 (if nums[0] >= target, then right else left)
        At 0 (return)

        target = 1
        At 0 (if nums[-1] >= target, then right else left)
        """

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                if nums[l] > target:
                    l = mid + 1
                elif nums[l] < target:
                    r = mid - 1
                else:
                    return l
            elif nums[mid] < target:
                if nums[r] < target:
                    l = mid + 1
                elif nums[r] > target:
                    r = mid - 1
                else:
                    return r
            else: 
                return mid
        
        return -1
