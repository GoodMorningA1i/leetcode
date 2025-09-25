class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        """
        {

        }
        """
        var complements: [Int: Int] = [:]
        for i in 0..<nums.count {
            if complements[nums[i]] == nil {
                complements[nums[i]] = i
            }
        }

        for j in 0..<nums.count {
            let complement = target - nums[j]
            guard let i = complements[complement] else { 
                continue
            }
            if i != j {
                return [i, j]
            }
        }
        return [] //will never reach
    }
}