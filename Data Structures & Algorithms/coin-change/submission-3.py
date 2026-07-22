class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp problem: O(amount * n)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0   # base case
        n = len(coins)
        coins.sort()

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    break
                
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1