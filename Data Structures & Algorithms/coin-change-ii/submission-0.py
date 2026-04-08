class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] = number of ways to make i using down to jth coin
        n = len(coins)
        dp = [[0] * (n+1) for _ in range(amount+1)]

        # base case: one way to make 0
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, amount+1):
            for j in range(n-1, -1, -1):
                coin = coins[j]
                if i >= coin:
                    # either use this coin or not
                    dp[i][j] = dp[i-coin][j] + dp[i][j+1]
                else:
                    # can't use this coin
                    dp[i][j] = dp[i][j+1]

        # ans is using all coin to make amount 
        return dp[amount][0]