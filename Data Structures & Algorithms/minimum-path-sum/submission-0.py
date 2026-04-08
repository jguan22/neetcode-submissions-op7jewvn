class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                dp[i][j] += grid[i][j]
        
        return dp[m-1][n-1]