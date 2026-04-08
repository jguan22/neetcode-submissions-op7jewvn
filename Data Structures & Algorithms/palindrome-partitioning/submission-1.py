class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        curr = []

        # helper
        def isPalindrome(substring):
            return substring == substring[::-1]
        
        def backtrack(start):
            if start >= n:
                res.append(curr[:])
                
            for i in range(start, n):
                if isPalindrome(s[start:i+1]):
                    curr.append(s[start:i+1])
                    backtrack(i+1)
                    curr.pop()
        

        backtrack(0)
        return res