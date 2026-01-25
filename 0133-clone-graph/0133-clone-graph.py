"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        whenever we add to visit, we need to create a new node
        if we see something in visited, add the edge to neighbours but don't dfs into it
        Note: for DFS, the stack is the recursion itself *mind-blown

        Time: O(V + E), O(V) since E will be at most V
        Space: O(V)
        """
        self.visited = set()
        self.valToNode = {}
        def dfs(node):
            if not node:
                return None

            newNode = Node(node.val)
            self.visited.add(node.val)
            self.valToNode[node.val] = newNode
            for neighbour in node.neighbors:
                if neighbour.val not in self.visited:
                    newNode.neighbors.append(dfs(neighbour))
                else:
                    newNode.neighbors.append(self.valToNode[neighbour.val])
            return newNode

        return dfs(node)

