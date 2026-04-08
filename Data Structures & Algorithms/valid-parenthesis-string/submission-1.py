class Solution:
    def checkValidString(self, s: str) -> bool:
        # two stacks
        left = []
        star = []

        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while left and star:
            # left comes after star, invalid
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()

        return True if not left else False