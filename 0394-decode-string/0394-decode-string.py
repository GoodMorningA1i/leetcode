class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                curr_stack = ''
                while stack and stack[-1] != '[':
                    curr_stack = stack.pop() + curr_stack
                
                if stack:
                    stack.pop() #pop out '['
                
                num = ''
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num
                
                stack.append(curr_stack * int(num))
            
        return ''.join(stack)