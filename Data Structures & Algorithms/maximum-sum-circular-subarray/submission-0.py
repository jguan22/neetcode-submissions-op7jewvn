class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # the max sum exists either as normal subarray
        # or one subarray at the front + one at the end, which is total_sum - min_sum in the middle
        total_sum = 0
        curr_max = max_sum = float('-inf')
        curr_min = min_sum = float('inf')

        for num in nums:
            total_sum += num

            curr_max = max(curr_max+num, num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min+num, num)
            min_sum = min(curr_min, min_sum)
        
        # edge case: all negative list
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)