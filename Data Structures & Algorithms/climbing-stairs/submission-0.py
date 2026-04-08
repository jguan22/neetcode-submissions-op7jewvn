class Solution:
    def climbStairs(self, n: int) -> int:
        # dp problem
        # dp[i] = number of ways to reach ith step
        dp = [0] * (n + 1)

        # base case: one way to reach 0 and 1
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]