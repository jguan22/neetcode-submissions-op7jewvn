class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] = number of ways to form t[:j] using s[:i]
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][0] = 1    # can always form an empty string
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    # either use this match char or skip it
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # skip it when no match
                    dp[i][j] = dp[i-1][j]
        
        return dp[m][n]