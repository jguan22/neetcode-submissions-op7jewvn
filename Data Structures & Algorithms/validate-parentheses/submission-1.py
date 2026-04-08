class Solution:
    def isValid(self, s: str) -> bool:
        pare = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []

        for c in s:
            if stack and c in pare and stack[-1] == pare[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0