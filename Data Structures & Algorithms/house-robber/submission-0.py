class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max money at ith house including ith
        n = len(nums)

        # edge case:
        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # two choice: either rob current one (skip last one) or rob last one
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])
        
        return max(dp[n-1], dp[n-2])