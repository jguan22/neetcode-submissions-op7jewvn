class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2d dp: one for profit and one for stock holding state
        n = len(prices)
        dp = [[float('-inf')] * (n+1) for _ in range(2)]
        dp[0][0] = 0    # base case: profit is 0 when starts

        for i in range(1, n+1):
            # 0 is not holding stock, while 1 is holding
            if i >= 2:
                # cooldown for a day to buy again
                dp[1][i] = max(dp[1][i-1], dp[0][i-2] - prices[i-1])
            else:
                dp[1][i] = max(dp[1][i-1], -prices[i-1])
            
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i-1])
            

        return dp[0][n]