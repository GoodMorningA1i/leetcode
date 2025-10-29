class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var index = -1
        var l = 0
        var r = nums.count - 1
        var mid = (l + r) / 2
        
        while l <= r {
            if nums[mid] < target {
                l = mid + 1
            } else if nums[mid] > target {
                r = mid - 1
            } else {
                index = mid
                break
            }
            mid = (l + r) / 2
        }
        
        return index
    }
}
