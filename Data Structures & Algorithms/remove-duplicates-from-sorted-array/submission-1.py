class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r =1, 1
        while r < len(nums):
            # swap unique number ahead
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
            