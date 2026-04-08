class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # swap each postive num to its index
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]

        # loop again to find any unmatch
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1