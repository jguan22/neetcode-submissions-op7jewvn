class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use a stack
        stack = []

        # use a operator map
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }

        # loop through tokens: O(n)
        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                token = operators[token](x, y)
            
            stack.append(int(token))
        
        return stack.pop()