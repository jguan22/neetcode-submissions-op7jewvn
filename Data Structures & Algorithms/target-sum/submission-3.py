class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # sanity check
        total_sum = offset = sum(nums)
        if abs(target) > total_sum:
            return 0

        n = len(nums)
        dp = [[0] * (2 * total_sum + 1) for _ in range(n)]

        # base case
        dp[0][offset + nums[0]] += 1
        dp[0][offset - nums[0]] += 1

        for i in range(1, n):
            for j in range(2 * total_sum + 1):
                if dp[i-1][j] != 0:
                    dp[i][j + nums[i]] += dp[i-1][j]
                    dp[i][j - nums[i]] += dp[i-1][j]

        return dp[n-1][offset + target]