class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max money at ith house including ith
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, n):
            # either skip this one or rob it
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]