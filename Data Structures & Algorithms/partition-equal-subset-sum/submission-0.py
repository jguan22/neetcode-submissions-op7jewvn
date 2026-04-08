class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp problem to find sum to half of total
        total_sum = sum(nums)

        # return early if total sum is odd
        if total_sum % 2 == 1:
            return False

        target_sum = total_sum // 2
        dp = [False] * (target_sum + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target_sum, -1, -1):
                # either use this coin or skip it
                if num <= i and dp[i-num]:
                    dp[i] = True
            
        return dp[target_sum]