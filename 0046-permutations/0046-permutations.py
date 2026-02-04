class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]: 
        def backtrack(i, nums):
            if i == len(nums):
                return [[]]
        
            res = []
            perms = backtrack(i + 1, nums)

            for p in perms:
                for j in range(0, len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res
        
        return backtrack(0, nums)