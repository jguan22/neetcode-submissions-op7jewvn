class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] = max coins by fursting ith to jth balloons
        nums = [1] + nums + [1]     # dummy balloons at both ends    
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # simulate the process backwards: pick the last balloon in this range
        for i in range(n-2, 0, -1): # 0 and n-1 are dummies
            for j in range(i, n-1):
                for k in range(i, j+1):
                    curr_gain = nums[i-1] * nums[k] * nums[j+1]
                    dp[i][j] = max(dp[i][j], curr_gain + dp[i][k-1] + dp[k+1][j])
            
        return dp[1][n-2]