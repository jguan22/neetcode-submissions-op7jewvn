class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp problem to match word1 to word2: O(m * n)
        # dp[i][j] = min ops to match word1[:i] to word2[:j]
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # base case
        dp[0][0] = 0    # match empty string to empty string
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                # same letter, no edition needed
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # either insert, delete, or replace it
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[m][n]