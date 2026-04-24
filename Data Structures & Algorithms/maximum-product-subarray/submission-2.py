class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # need to keep track on both max and min as min_neg can become max with nxt neg num
        n = len(nums)
        curr_max = nums[0]
        curr_min = nums[0]
        max_product = nums[0]
        for i in range(1, n):
            temp_max = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_min = min(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_max = temp_max
            
            max_product = max(max_product, curr_max)
        
        return max_product