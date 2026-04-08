class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1, i+1):
                square = j*j
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[n]