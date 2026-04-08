class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # go from left to right, drop sub when sum is less than curr
        max_sum = float('-inf')

        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(curr_sum, max_sum)

        return max_sum