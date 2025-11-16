# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], otherRoot: Optional[TreeNode]) -> bool:
        if not root and not otherRoot:
            return True
        if root and otherRoot and root.val == otherRoot.val:
            return self.sameTree(root.left, otherRoot.left) and self.sameTree(root.right, otherRoot.right)
        
        return False