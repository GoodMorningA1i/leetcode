import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in operators:
                #guaranteed to have something in the stack
                operator = tokens[i]
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                if operator == '+':
                    stack.append(operand1 + operand2)
                elif operator == '-':
                    stack.append(operand1 - operand2)
                elif operator == '*':
                    stack.append(operand1 * operand2)
                else:
                    stack.append(int(operand1 / operand2))
            else:
                stack.append(int(tokens[i]))

        return stack.pop()