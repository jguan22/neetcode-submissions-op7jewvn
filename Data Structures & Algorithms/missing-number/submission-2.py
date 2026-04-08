class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        for i in range(n):
            ans ^= nums[i]
            ans ^= i
        
        return ans