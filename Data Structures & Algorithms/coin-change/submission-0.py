class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = min number of coins to make i
        coins.sort()
        dp = [float('inf')] * (amount+1)

        # base case
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] < float('inf') else -1