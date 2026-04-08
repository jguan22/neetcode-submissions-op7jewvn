class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j] = True if s[i:j+1] is a panlindrome
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = n

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        ans += 1
        return ans