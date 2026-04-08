class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = []
        n = len(digits)
        letter_map = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
            }
        
        def backtrack(i):
            if i == n:
                res.append("".join(curr))
                return
            
            for l in letter_map[digits[i]]:
                curr.append(l)
                backtrack(i+1)
                curr.pop()

        if not digits:
            return res
        backtrack(0)
        return res