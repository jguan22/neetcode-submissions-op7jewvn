class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # convert to 1d dp: O(m * n)
        # initially, first row has one path only
        dp = [1] * (n+1)
        dp[0] = 0   # base case: dummy col on the left

        # loop through the row
        for i in range(1, m):
            # update each col with path from left and up(itself)
            for j in range(1, n+1):
                dp[j] += dp[j-1]

        return dp[n]

        '''# intuitive 2d dp problem: O(m * n)
        dp = [[0] * n for _ in range(m)]

        # base case
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]'''