class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        let numSet: Set = Set(nums)
        var maxLen = 0

        for num in numSet {
            if !numSet.contains(num - 1) {
                var length = 0
                while numSet.contains(num + length) {
                    length += 1
                }
                maxLen = max(maxLen, length)
            }
        }

        return maxLen
    }
}
