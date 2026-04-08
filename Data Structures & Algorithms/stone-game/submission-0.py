class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # both play optimally, so in the end, we're looking for the min difference of max of two subsets
        # dp[i][j] = the max can take from i to j
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i] # base case: take the last stone

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # either take i or j
                take_i = piles[i] - dp[i+1][j]
                take_j = piles[j] - dp[i][j-1]
                dp[i][j] = max(take_i, take_j)
        
        return dp[0][n-1] > 0 # Alice win if total sum > 0