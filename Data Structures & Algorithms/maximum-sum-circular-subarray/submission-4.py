class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # the max sum subarray is either in the mid of array or at both ends
        # track max_sum for the first one, and total_sum - min_sum for the second one
        total_sum = nums[0]
        max_sum = min_sum = nums[0]

        # loop through all num once: O(n)
        curr_max = curr_min = nums[0]
        for i in range(1, len(nums)):
            total_sum += nums[i]

            # increment curr subarray sum or start a new subarray, and update max_sum
            curr_max = max(curr_max + nums[i], nums[i])
            max_sum = max(curr_max, max_sum)

            # decrement curr subarray sum or start a new subarray, and update min_sum
            curr_min = min(curr_min + nums[i], nums[i])
            min_sum = min(curr_min, min_sum)

        # edge case: all negative array, res leads to 0 (total = min)
        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)