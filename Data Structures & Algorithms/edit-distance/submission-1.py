class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = min distance to convert word1[:i] to word2[:j]
        m = len(word1)
        n = len(word2)
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range( n+1):
                # base case
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # options: insert, delete, replace
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[m][n]