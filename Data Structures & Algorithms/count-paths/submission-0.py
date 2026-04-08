class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = number of ways to reach i,j
        # base case: top row and left col has only 1 way
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                # either reach from left or up
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]