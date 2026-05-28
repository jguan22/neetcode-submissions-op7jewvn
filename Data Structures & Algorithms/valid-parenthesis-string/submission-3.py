class Solution:
    def checkValidString(self, s: str) -> bool:
        # use two stacks: one for ( and one for *
        left_stack = []
        star_stack = []

        # store all left parenthesis ans stars and deal with right parenthesis
        for i, c in enumerate(s):
            if c == ")":
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            elif c == "(":
                left_stack.append(i)
            else:
                star_stack.append(i)
        
        # take care of all left parenthesis
        while left_stack:
            if not star_stack or left_stack[-1] > star_stack[-1]:
                return False

            left_stack.pop()
            star_stack.pop()
        
        return True