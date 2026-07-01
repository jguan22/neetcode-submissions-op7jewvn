class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp problem to match word1 to word2
        # dp[i][j] = min ops to match word1[:i] to word2[:j]
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][0] = 0    # base case: match empty string to empty string

        # base case
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + 1
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + 1
        
        # loop through the table: O(m*n)
        for i in range(1, m+1):
            for j in range(1, n+1):
                # same char, no need to edit it
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:   # diff char, either insert, delete, or replace
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[m][n]