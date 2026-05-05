class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # swap num to its position (1-index)
        n = len(nums)
        i = 0
        while i < n:
            # swap if target pos is not curr num
            curr = nums[i]
            if 0 < curr <= n and nums[curr-1] != curr:
                nums[i], nums[curr-1] = nums[curr-1], curr
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1