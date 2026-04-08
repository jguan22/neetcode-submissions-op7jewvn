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

        for n in tokens:
            if n not in operands:
                stack.append(int(n))
                continue
            
            operation = operands[n]
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(operation(n2, n1))
        
        return stack.pop()