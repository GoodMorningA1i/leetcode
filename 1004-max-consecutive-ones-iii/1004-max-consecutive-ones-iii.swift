class Solution {
    func longestOnes(_ nums: [Int], _ k: Int) -> Int {
        var l = 0
        var numZeroes = 0
        var currentLongest = 0
        var res = 0
        for r in 0..<nums.count {
            if nums[r] == 0 {
                numZeroes += 1
            }
            currentLongest += 1

            while numZeroes > k {
                if nums[l] == 0 {
                    numZeroes -= 1
                }
                currentLongest -= 1
                l += 1
            }

            res = max(res, currentLongest)
        }

        return res
    }
}