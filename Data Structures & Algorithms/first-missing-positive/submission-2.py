class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # swap each postive num to its index (1-index)
        n = len(nums)
        for i in range(n):
            # nums[i] goes to position(nums[i] - 1)
            while 1 <= nums[i] <=n and nums[nums[i] - 1] != nums[i]:
                index = nums[i] - 1
                nums[index], nums[i] = nums[i], nums[index]
        
        # loop again to find any unmatch
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        # edge case: all match, return next positive number
        return n + 1
        
        