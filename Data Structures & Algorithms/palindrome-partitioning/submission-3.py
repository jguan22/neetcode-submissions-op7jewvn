class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        curr = []

        # add dp table to store the palindrome result
        dp = [[None] * n for _ in range(n)]

        # helper
        def isPalindrome(x, y):
            if x >= y:
                return True
                
            if dp[x][y] is not None:
                return dp[x][y]
            
            dp[x][y] = (s[x] == s[y]) and isPalindrome(x + 1, y - 1)
            return dp[x][y]
        

        def backtrack(start):
            if start >= n:
                res.append(curr[:])
                return
                
            for i in range(start, n):
                if isPalindrome(start, i):
                    curr.append(s[start:i+1])
                    backtrack(i+1)
                    curr.pop()
        

        backtrack(0)
        return res