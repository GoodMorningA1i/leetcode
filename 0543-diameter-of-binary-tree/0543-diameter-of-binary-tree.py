# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        #this returns the height, # of nodes
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.result = max(self.result, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.result