class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # max sum either in the range (0, n) or at both end
        # the latter one can be calculated by total - min sum
        # linear scan to find both max and min sum
        n = len(nums)
        max_sum = curr_max = nums[0]
        min_sum = curr_min = nums[0]
        total = nums[0]

        for i in range(1, n):
            total += nums[i]

            curr_max = max(curr_max + nums[i], nums[i])
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min + nums[i], nums[i])
            min_sum = min(min_sum, curr_min)
        
        # edge case: all-negative list will ends as 0
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)