class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # need two dp tables, since neg product can become max product later with another neg
        n = len(nums)
        dp_pos = [float('-inf')] * n
        dp_neg = [float('inf')] * n
        dp_pos[0] = dp_neg[0] = nums[0]

        # O(n)
        for i in range(1, n):
            dp_pos[i] = max(nums[i], dp_pos[i-1] * nums[i], dp_neg[i-1] * nums[i])
            dp_neg[i] = min(nums[i], dp_neg[i-1] * nums[i], dp_pos[i-1] * nums[i])
        
        return max(dp_pos)