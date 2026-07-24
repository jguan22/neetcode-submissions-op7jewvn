class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp problem with two states: hold a stock or not O(n)
        n = len(prices)
        dp = [[0] * (n+1) for _ in range(2)]
        dp[1][0] = float('-inf')    # base case to initiate buying 

        for i in range(1, n+1):
            # hold state transfers from i-1 hold or i-2 not hold
            if i == 1:
                dp[1][i] = max(dp[1][i-1], - prices[i-1])
            else:
                dp[1][i] = max(dp[1][i-1], dp[0][i-2] - prices[i-1])

            # not hold state transfer from i-1 not hold or i-1 hold
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i-1])
        
        return dp[0][n]