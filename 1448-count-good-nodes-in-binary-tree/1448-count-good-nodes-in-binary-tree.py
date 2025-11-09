# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValue):
            res = 0
            if not node:
                return 0
            
            if node.val >= maxValue:
                res += 1
            maxValue = max(maxValue, node.val)  

            res += dfs(node.left, maxValue)
            res += dfs(node.right, maxValue)

            return res
        return dfs(root, root.val)
        

