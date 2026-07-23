class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # convert to a subset sum problem
        # sanity check
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        # subset sum target, dp problem: O(target * n)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True    # base case
        
        for num in nums:    
            for i in range(target, num-1, -1):  # each num only use once
                dp[i] |= dp[i-num]
        
        return dp[target]