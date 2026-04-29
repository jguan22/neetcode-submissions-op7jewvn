class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # max_sum either in middle or two sub at both ends which is total - min_sum
        total_sum = 0
        curr_max = max_sum = float('-inf')
        curr_min = min_sum = float('inf')

        for num in nums:
            total_sum += num

            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)
        
        # edge case: all negatives
        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)