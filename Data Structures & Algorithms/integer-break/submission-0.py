class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        dp = [1] * (n+1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            for j in range(2, 4):
                dp[i] = max(dp[i-2]*2, dp[i-3]*3)
        return dp[n]