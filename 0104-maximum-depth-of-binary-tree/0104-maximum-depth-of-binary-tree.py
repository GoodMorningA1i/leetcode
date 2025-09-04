# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        if not root:
            return 0

        res += 1
        res += max(Solution.maxDepth(self, root.left), Solution.maxDepth(self, root.right))

        return res