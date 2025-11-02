class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        we can only add open or close when it less than or equal to n
        if we have close < open, then we can add close
        """
        res = []
        stack = []

        def backtrack(openNumber, closeNumber):
            #Valid IFF openNumber == closeNumber == n
            if openNumber == closeNumber == n:
                res.append("".join(stack))
                return
            
            #Only add open brackets if its under the limit
            if openNumber < n:
                stack.append('(')
                backtrack(openNumber + 1, closeNumber)
                stack.pop()

            #Only add close brackets if its less than the # of open brackets
            if closeNumber < openNumber:
                stack.append(')')
                backtrack(openNumber, closeNumber + 1)
                stack.pop()

        backtrack(0, 0) 
        return res
