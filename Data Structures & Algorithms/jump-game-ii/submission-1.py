class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp solution: O(n^2)
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            max_step = i + nums[i]
            for j in range(i+1, min(max_step+1, n)):
                dp[j] = min(dp[j], dp[i] + 1)
        
        return dp[n-1]