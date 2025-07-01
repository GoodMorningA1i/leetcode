# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        newTree = TreeNode()
        newTree.val = root.val
        newTree.left = Solution.invertTree(self, root.right)
        newTree.right = Solution.invertTree(self, root.left)
        return newTree
        
