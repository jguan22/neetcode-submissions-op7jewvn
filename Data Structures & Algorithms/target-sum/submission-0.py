class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][j] = number of ways to make j using up to ith num
        n = len(nums)
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0

        # sum can range from -total_sum to total_sum
        dp = [[0] * (2*total_sum + 1) for _ in range(n)]

        # base case: use the first num
        dp[0][total_sum + nums[0]] += 1
        dp[0][total_sum - nums[0]] += 1

        for i in range(1, n):
            for j in range(-total_sum, total_sum+1):
                # use either + or -
                index = j + total_sum
                if dp[i-1][index] > 0:
                    dp[i][index + nums[i]] += dp[i-1][index]
                    dp[i][index - nums[i]] += dp[i-1][index]

        return dp[n-1][target + total_sum]