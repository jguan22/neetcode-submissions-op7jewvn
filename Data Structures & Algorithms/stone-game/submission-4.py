class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp problem: O(n^2)
        n = len(piles)
        dp = [[float('-inf')] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # base case: take the last pile
                if i == j:
                    dp[i][j] = piles[i]
                else:
                    # take either left or right, minus prev take
                    dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        
        # Alice start first so postive stones Alice wins
        return True if dp[0][n-1] > 0 else False