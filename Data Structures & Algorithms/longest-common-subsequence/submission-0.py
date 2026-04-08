class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = longest at ith of text1 and jth of text2
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # same: dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        # not: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] != text2[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
        
        return dp[m][n]