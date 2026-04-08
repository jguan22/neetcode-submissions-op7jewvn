class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # compute the prefix and suffix product
        n = len(nums)
        prefix = [1] * len(nums)
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = [1] * len(nums)
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        ans = [1] * len(nums)
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        return ans