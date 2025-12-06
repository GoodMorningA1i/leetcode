# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(node, isLeft):
            if node.left is None and node.right is None and isLeft:
                self.sum += node.val
            if node.left:
                dfs(node.left, True)
            if node.right:
                dfs(node.right, False)
            
        dfs(root, False)
        return self.sum