class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] = # of ways to make j amount
        dp = [0] * (amount+1)
        dp[0] = 1   # base case
        
        for coin in coins:
            for i in range(1, amount+1):
                if coin <= i:
                    dp[i] += dp[i-coin]
        
        return dp[amount]
                