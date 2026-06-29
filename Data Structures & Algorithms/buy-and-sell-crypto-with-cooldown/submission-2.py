class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp problem with two states: hold or not hold a stock
        n = len(prices)
        dp = [[0] * (n + 1) for _ in range(2)]
        dp[1][0] = float('-inf')    # base case to initiate buying

        # loop through n day: O(N)
        for i in range(1, n+1):
            # hold states: either hold stock from before or buy it today
            if i == 1:
                dp[1][i] = max(dp[1][i-1], -prices[i-1])
            else:
                dp[1][i] = max(dp[1][i-1], dp[0][i-2] - prices[i-1])
            
            # not hold states: either sell it today or same state from prev
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i-1])
        
        return dp[0][n]