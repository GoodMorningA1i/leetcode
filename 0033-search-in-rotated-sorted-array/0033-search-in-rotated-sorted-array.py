class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        index = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                index = mid
                break

            if nums[l] <= nums[mid]:
                #left sorted
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                #right sorted
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        return index