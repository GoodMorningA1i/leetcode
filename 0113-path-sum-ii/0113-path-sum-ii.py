# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        pass in a sum value in dfs
        the sum accumulate
        base case, is checking if reached leaf
        append to overall list, if at base case, sum = targetSum

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        self.res = []

        def dfs(node, sum, nodesOfSum):
            if not node:
                return
            
            sum += node.val
            nodesOfSum.append(node.val)
            if sum == targetSum and not node.left and not node.right:
                self.res.append(nodesOfSum.copy())
            else:
                dfs(node.left, sum, nodesOfSum)
                dfs(node.right, sum, nodesOfSum)
            
            nodesOfSum.pop()
        
        dfs(root, 0, [])
        return self.res
