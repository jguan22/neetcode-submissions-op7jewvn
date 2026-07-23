class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # aggregate sum until sum is less than next num, then start over: O(n)
        curr_sum = float('-inf')
        max_sum = curr_sum

        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum