class Solution:
    def checkValidString(self, s: str) -> bool:
        # each ')' needs a '(' or '*' on its left to be valid
        # the rest '(' needs '*' on its right to be valid
        # thus, need to track on '(' and '*' with position
        left = []
        star = []

        # loop through s: O(n)
        for i, c in enumerate(s):
            if c == ')':
                # greedy: always go with '(' first
                if left:
                    left.pop()
                elif star:     # then '*'
                    star.pop()
                else:           # instant false if nothing on left
                    return False
            elif c == '(':
                left.append(i)
            else:
                star.append(i)
        
        # now check left parenthesis: O(n)
        while left:
            # each '(' needs '*' on its right
            if star and left[-1] < star[-1]:
                left.pop()
                star.pop()
            else:
                return False
        
        return True