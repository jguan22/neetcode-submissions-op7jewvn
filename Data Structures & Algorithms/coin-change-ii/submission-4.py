class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp problem: O(amount * n)
        dp = [0] * (amount + 1)
        dp[0] = 1   # base case
        
        # Outer loop over coins prevents duplicate combinations
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]