class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp problem with state
        # 1 as hold a stock, 0 as not
        n = len(prices)
        dp = [[0] * (n+1) for _ in range(2)]

        dp[1][0] = float('-inf') 
        for i in range(1, n+1):
            # for the case of holding a stock
            # state 1: either buy stock today or hold from yesterday
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] - prices[i-1])

            # state 0: either sell stock or didn't buy before
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i-1])
        
        # sell stock at day n
        return dp[0][n]