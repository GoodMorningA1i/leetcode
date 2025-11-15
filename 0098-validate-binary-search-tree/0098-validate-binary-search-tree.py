# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftBound, rightBound):
            if not node:
                return True
            if node.val <= leftBound:
                return False
            if node.val >= rightBound:
                return False

            leftCheck = dfs(node.left, leftBound, min(node.val, rightBound))
            rightCheck = dfs(node.right, max(node.val, leftBound), rightBound)

            return leftCheck and rightCheck
        
        return dfs(root, float("-inf"), float("inf"))