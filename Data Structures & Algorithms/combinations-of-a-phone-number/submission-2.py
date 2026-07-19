class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # create a letter map for fast query: O(1)
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
        
        n = len(digits)
        ans = []
        
        if not digits:
            return ans

        # backtracking (3 or 4)^n states: O(n * 4^n)
        def backtrack(index, curr_str):
            if index >= n:
                ans.append(curr_str)
                return
            
            for letter in letter_map[digits[index]]:
                backtrack(index + 1, curr_str + letter)

        backtrack(0, "")
        return ans