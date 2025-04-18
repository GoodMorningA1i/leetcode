class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] #only opening brackets in here
        closeToOpen = {')': '(', '}':'{', ']':'['}

        for char in s:
            if char in closeToOpen:
                if len(stack) > 0 and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0

        
        #Time Complexity: O(n)
        #Space Complexity: O(n)
                



       


            