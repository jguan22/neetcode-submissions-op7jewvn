class Solution:
    def rob(self, nums: List[int]) -> int:
        # the first house and the last one is connected, so only one can be chosen
        # meaning either max from nums[:n] or nums[1:]
        def robMax(houses):
            n = len(houses)
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(dp[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[n-1]

        n = len(nums)
        if n < 3:
            return max(nums)
        return max(robMax(nums[1:]), robMax(nums[:n-1]))