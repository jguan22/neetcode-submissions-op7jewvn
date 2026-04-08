class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # use two table to store largest num and smallest num
        n = len(nums)
        dp_max = [0] * n
        dp_min = [0] * n

        # base case:
        dp_max[0] = dp_min[0] = nums[0]

        for i in range(1, n):
            # max num comes from either negative min or pos max or curr num
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])

            dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
        
        return max(dp_max)