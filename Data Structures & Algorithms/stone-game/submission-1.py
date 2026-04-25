class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] = the max can take from i to j
        # both play optimally, so dp[i][j] is max of take i or j minus max of next round
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]     # base case
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                # either take i or take j
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        
        return dp[0][n-1] > 0   # Alice win if positive