class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp problem
        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        # O(m * n)
        for i in range(1, n+1):
            for j in range(1, m+1):
                # find a same char, extend from prev subsequnce
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:   # if not, go with the longest one
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]