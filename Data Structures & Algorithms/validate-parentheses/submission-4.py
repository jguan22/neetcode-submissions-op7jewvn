class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack to track brackets
        stack = []

        # hash map to easily query open bracket using close one
        bracket_pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        # loop through each char: O(n)
        for c in s:
            if c in bracket_pairs and stack and stack[-1] == bracket_pairs[c]:
                stack.pop()
            else:
                stack.append(c)

        return False if stack else True