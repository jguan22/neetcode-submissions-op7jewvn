class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # precompute prefix and suffix products: O(n)
        n = len(nums)
        prefix_prod = [1] * n
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        
        suffix_prod = [1] * n
        for i in range(n-2, -1, -1):
            suffix_prod[i] = suffix_prod[i+1] * nums[i+1]

        # linear scan the list to multiply prefix with suffix: O(n)
        ans = [1] * n
        for i in range(n):
            ans[i] = prefix_prod[i] * suffix_prod[i]
        
        return ans