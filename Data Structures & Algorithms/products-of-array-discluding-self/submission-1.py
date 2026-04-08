class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix and suffix
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        # set the first one to 1
        prefix[0] = 1
        suffix[n-1] = 1

        # compute the prefix by multiply number on the left to its prefix
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]

        # compute the suffix by multiply number on the right to its suffix
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        # for each number, its product is prefix times suffix
        ans = [1] * n
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
            
        return ans
