class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp problem: need to track both max and min (negative can become largest with another neg)
        n = len(nums)
        dp_pos = [0] * n
        dp_neg = [0] * n
        dp_pos[0] = dp_neg[0] = nums[0]

        # loop through all nums: O(n)
        for i in range(1, n):
            dp_pos[i] = max(dp_pos[i-1] * nums[i], dp_neg[i-1] * nums[i], nums[i])
            dp_neg[i] = min(dp_pos[i-1] * nums[i], dp_neg[i-1] * nums[i], nums[i])
        
        return max(dp_pos)