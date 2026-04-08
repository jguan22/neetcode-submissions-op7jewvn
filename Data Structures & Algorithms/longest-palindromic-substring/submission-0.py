class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = True if s[i:j+1] is palindromic
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # base case: single char
        for i in range(n):
            dp[i][i] = True

        start = 0
        max_size = 1
        # base case: doulbe char
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_size = 2
                start = i

        # dp[i-1][j+1] = dp[i][j] if s[i-1] == s[j+1]
        for size in range(3, n+1):
            for i in range(n - size + 1):
                j = i + size - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    max_size = size
                    start = i
                
        return s[start:start + max_size]