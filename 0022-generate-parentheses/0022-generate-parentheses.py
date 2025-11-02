class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursiveSolve(curr, openBracketNum, closeBracketNum): 
            if closeBracketNum == openBracketNum == n:
                return [curr]
            
            openList, closeList = [], []
            if openBracketNum < n:
                openList = recursiveSolve(curr + '(', openBracketNum + 1, closeBracketNum)
                
            if closeBracketNum < openBracketNum:
                closeList = recursiveSolve(curr + ')', openBracketNum, closeBracketNum + 1)
                
            return openList + closeList
        
        return recursiveSolve('', 0, 0)