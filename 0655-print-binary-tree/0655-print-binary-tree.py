# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        res = []
        
        #find height of tree
        q = deque()
        q.append(root)
        height = -1
        while q:
            height += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        #print binary tree
        m = height + 1
        n = 2**(height+1) - 1

        for i in range(m):
            subRes = []
            for j in range(n):
                subRes.append("")
            res.append(subRes)

        r = 0
        print(res)

        q = deque()
        q.append((root, (n-1)//2))
        while q:
            for _ in range(len(q)):
                node, c = q.popleft()
                print(r)
                res[r][c] = str(node.val)
                if node.left:
                    q.append((node.left, c - 2**(height-r-1)))
                if node.right:
                    q.append((node.right, c + 2**(height-r-1)))
            r += 1

        return res