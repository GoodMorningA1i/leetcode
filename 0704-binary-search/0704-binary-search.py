class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1

        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                index = mid
                break
            mid = (l + r) // 2

        return index