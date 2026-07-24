class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # convert to a subset sum problem: O(m*n)
        # pos_subset + neg_subset = target
        # pos_subset - neg_subset = total
        # 2 * pos_subset = target + total

        # sanity check
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        new_target = (total + target) // 2

        dp = [0] * (new_target+1)
        dp[0] = 1   # base case

        for num in nums:
            for i in range(new_target, num-1, -1):  # each num can be used once
                dp[i] += dp[i-num]
        
        return dp[new_target]