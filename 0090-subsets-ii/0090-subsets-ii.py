class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def dfs(i, curr):
            if i == len(nums):
                res.add(tuple(curr.copy()))
                return
        
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            
            dfs(i+1, curr)
            
        
        dfs(0, [])
        res = [list(subSet) for subSet in res]
        return res