class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] = max coins to collect from burst ith to jth balloons (subproblem)
        # add two balloons at both end with 1 to handle edge case
        new_nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * (n+2) for _ in range(n+2)]

        # loop through the new list excluding the two ends (from shortest to longest)
        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for i in range(l, r+1):
                    # burst the ith balloon last, two neighbours will be l-1, r+1
                    curr_burst = new_nums[l-1] * new_nums[i] * new_nums[r+1]
                    # this total will be two subproblems + this burst
                    dp[l][r] = max(dp[l][r], curr_burst + dp[l][i-1] + dp[i+1][r])

        return dp[1][n]