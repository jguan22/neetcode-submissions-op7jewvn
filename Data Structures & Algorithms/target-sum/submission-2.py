class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # reduce the problem into a subset problem
        # sum(P) - sum(N) = target
        # sum(P) + sum(N) = total
        # looking for a subset that sum(P) = target+total // 2
        total = sum(nums)
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        
        subset_target = (target + total) // 2
        dp = [0] * (subset_target + 1)
        dp[0] = 1
        
        for num in nums:
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_target]