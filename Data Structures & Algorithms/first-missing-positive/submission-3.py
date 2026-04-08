class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # swap the num to where it supposed to be (num 1 -> index 0)
        n = len(nums)
        i = 0
        while i < n:
            target_i = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[target_i]:
                nums[i], nums[target_i] = nums[target_i], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != (i+1):
                return i+1
        
        return n+1