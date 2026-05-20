class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] is the most stones from pile ith to jth
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:  # take the last stone
                    dp[i][j] = piles[i]
                else:   # either take i or j, then substract opponent's gain
                    dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        
        return dp[0][n-1] > 0