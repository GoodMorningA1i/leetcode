# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrder(root):
            """ Description
            :type root: ....
            :rtype: List
            >>> Example
            ....
            """
            if root == None:
                return []
            else:
                return inOrder(root.left) + [root.val] + inOrder(root.right)
        
        return inOrder(root)[k-1]
        
        
#         1st attempt        
#         def number_of_left_nodes(root):
#             """Description
#             :type root: .....
#             :rtype: int
#             >>> Example
#             ....
#             """
#             numLeftNodes = 0
#             if root == None:
#                 return 0
#             else if root.left == None and root.right == None:
#                 return 1
#             else if root.left != None:
#                 numLeftNodes = number_of_left_nodes(root.left)
#                 numLeft += 1
        
#         if root == None:
#             return 
                
        
#         if root:
#             if root.left != None:
#                 kthSmallest