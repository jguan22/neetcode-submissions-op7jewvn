class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use stack
        stack = []

        operands = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if token in operands:
                b = stack.pop()
                a = stack.pop()
                stack.append(operands[token](a, b))
            else:
                stack.append(int(token))
        
        return stack.pop()