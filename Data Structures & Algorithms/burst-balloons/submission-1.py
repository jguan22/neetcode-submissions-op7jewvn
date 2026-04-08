class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] = max coins to collect from burst ith to jth balloons
        # consider the process backwards: burst ith at last
        # thus, dp[l][r] = dp[l][i-1] + dp[i+1][r] + coin from bursting ith
        # add two balloons at both end with 1 to handle edge case
        n = len(nums)
        dp = [[0] * (n+2) for _ in range(n+2)]
        new_nums = [1] + nums + [1]

        # loop the list using l and r bounds from 1 to n+1
        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for i in range(l, r+1):
                    curr_coin = new_nums[l-1] * new_nums[i] * new_nums[r+1]

                    dp[l][r] = max(dp[l][r], dp[l][i-1] + dp[i+1][r] + curr_coin)

        return dp[1][n]