class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        var maxLen = 0
        var numSet: Set<Int> = Set(nums)

        for num in numSet {
            if !numSet.contains(num + 1) {
                var length = 1
                while numSet.contains(num - length) {
                    length += 1
                }
                maxLen = max(maxLen, length)
            }
        }
        return maxLen

    }
}
