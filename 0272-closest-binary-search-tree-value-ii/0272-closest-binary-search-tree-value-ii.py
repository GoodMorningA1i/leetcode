# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """
        17 minutes brainstorming
        Thought of brute force solution of O(nlogn)
        Going through all nodes and calculcating the diffs from target
        Then sort it and choose the first k
        """
        def dfs(q, node):
            if not node:
                return

            dfs(q, node.left)
            q.append(node.val)

            if len(q) > k:
                if abs(target - q[0]) <= abs(target - q[-1]):
                    q.pop()
                    return
                else:
                    q.popleft()
            
            dfs(q, node.right)

        q = deque()
        dfs(q, root)
        return list(q)
            