class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i, c in enumerate(s):
            if c == '(':
                left_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:
                if left_stack :
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while left_stack:
            if not star_stack or left_stack[-1] > star_stack[-1]:
                return False
            
            star_stack.pop()
            left_stack.pop()
            
        return True