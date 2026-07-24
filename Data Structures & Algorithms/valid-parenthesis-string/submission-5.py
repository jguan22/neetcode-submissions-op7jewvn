class Solution:
    def checkValidString(self, s: str) -> bool:
        # each ')' must need at least one '(' or '*'
        # use stacks to record '(' or '*'
        left_stack = []
        star_stack = []

        # greedy: always go with '(' first
        for i, c in enumerate(s):
            if c == '(':
                left_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:
                # use '(' first
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    # if not, use '*'
                    star_stack.pop()
                else:
                    return False
        
        # then, pair '(' with '*' on its right
        while left_stack:
            if not star_stack or left_stack[-1] > star_stack[-1]:
                return False
            
            star_stack.pop()
            left_stack.pop()

        return True
        