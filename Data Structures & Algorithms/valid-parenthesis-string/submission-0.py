class Solution:
    def checkValidString(self, s: str) -> bool:
        # use two stacks
        open_parethesis = []
        asterisk = []

        for i, c in enumerate(s):
            if c == '(':
                open_parethesis.append(i)
            elif c == '*':
                asterisk.append(i)
            else:
                if open_parethesis:
                    open_parethesis.pop()
                elif asterisk:
                    asterisk.pop()
                else:
                    return False
            
        # ensure open parenthesis on the left
        while open_parethesis and asterisk:
            if open_parethesis[-1] > asterisk[-1]:
                return False
            open_parethesis.pop()
            asterisk.pop()
        
        # open stack should be empty to be true
        return len(open_parethesis) == 0