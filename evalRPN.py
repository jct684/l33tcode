class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #time complexity O(n)
        #space complexity O(n)
        if len(tokens) == 1:
            return int(tokens[0])
        operand_stack = []
        
        for token in tokens:
            if token == '-':
                x = operand_stack.pop()
                y = operand_stack.pop()
                z = y - x
                operand_stack.append(z)
            elif token == '+':
                x = operand_stack.pop()
                y = operand_stack.pop()
                z = y + x
                operand_stack.append(z)
            elif token == '*':
                x = operand_stack.pop()
                y = operand_stack.pop()
                z = y * x
                operand_stack.append(z)
            elif token == '/':
                x = operand_stack.pop()
                y = operand_stack.pop()
                z = int(y/x)
                operand_stack.append(z)
            else:
                operand_stack.append(int(token))
        return operand_stack[0]