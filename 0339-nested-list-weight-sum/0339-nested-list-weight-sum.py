# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        [[1,1],2,[1,1]]
        Time: O(n) where n is the length of nestedList. Can recursion make this higher
        Space: O(n)

        Dry run
        [[1,1],2,[1,1]]
                    ^
        """
        self.elems = []
        self.depths = []

        def dfs(elem, depth):
            if elem.isInteger():
                #base case
                self.elems.append(elem.getInteger())
                self.depths.append(depth)
            else:
                #recurisve case
                for e in elem.getList():
                    dfs(e, depth + 1)

        for elem in nestedList:
            dfs(elem, 1)
        
        res = 0
        for i in range(len(self.elems)):
            res += self.elems[i] * self.depths[i]

        return res