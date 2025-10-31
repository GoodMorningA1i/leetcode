class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                index = mid
                break

        return index
        