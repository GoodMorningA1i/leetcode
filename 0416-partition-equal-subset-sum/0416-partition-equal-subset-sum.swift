class Solution {
    func canPartition(_ nums: [Int]) -> Bool {
        let sumOfNums = nums.reduce(0, +)
        if sumOfNums % 2 == 1 {
            return false
        }
        var dp: Set<Int> = []
        dp.insert(0)
        let target = sumOfNums / 2

        for i in stride(from: nums.count - 1, to: -1, by: -1) {
            var nextDP: Set<Int> = []
            for t in dp {
                nextDP.insert(t + nums[i])
                nextDP.insert(t)
            }
            dp = nextDP
        }

        return dp.contains(target) ? true : false
    }
}