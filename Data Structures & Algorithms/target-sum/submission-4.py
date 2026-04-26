class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # convert to a subset sum problem
        # pos_subset - neg_subset = target; pos_subset + neg_subset = total_sum
        # thus, 2 * pos_subset = target + total_sum
        total_sum = sum(nums)
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0
        
        new_target = (total_sum + target) // 2
        dp = [0] * (new_target + 1)
        dp[0] = 1

        for num in nums:
            for i in range(new_target, -1, -1):
                if num > i:
                    break
                
                dp[i] += dp[i-num]
        
        return dp[new_target]