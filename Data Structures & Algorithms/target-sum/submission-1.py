class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # either plus or minus a num
        total = sum(nums)
        
        # edge case
        if total < abs(target):
            return 0

        dp = [[0] * (2*total+1) for _ in range(len(nums))]
        dp[0][total + nums[0]] += 1
        dp[0][total - nums[0]] += 1

        for i in range(1, len(nums)):
            for j in range(2*total+1):
                if dp[i-1][j] > 0:
                    dp[i][j+nums[i]] += dp[i-1][j]
                    dp[i][j-nums[i]] += dp[i-1][j]
        
        return dp[len(nums)-1][total+target]