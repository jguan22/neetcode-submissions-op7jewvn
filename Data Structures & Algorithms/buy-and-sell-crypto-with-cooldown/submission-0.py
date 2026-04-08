class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for a certain day, either buy, hold, or sell
        # need to track the state (hold a stock (1) or not (0))
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = -float('inf')

        for i in range(1, n+1):
            price = prices[i - 1]

            # Not holding stock on day i:
            # 1. Not holding on day i-1, do nothing
            # 2. Holding on day i-1, sell today
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + price)
            
            # Holding stock on day i:
            # 1. Holding on day i-1, do nothing
            # 2. Not holding on day i-2 (cooldown), buy today
            if i >= 2:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - price)
            else:
                dp[i][1] = max(dp[i - 1][1], -price)  # can buy on first day

        return dp[n][0]