class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # bucket sort: move positive nums to its position (0-index)
        n = len(nums)
        i = 0

        # loop through the list, each num will be swapped once: O(n)
        while i < n:
            # swap if num in the range of [1, n]
            # also, target position is not taken by the same num
            if 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                target_i = nums[i] - 1
                nums[i], nums[target_i] = nums[target_i], nums[i]
                continue

            i += 1
        
        # loop through the list to find the first num missing: O(n)
        for i in range(n):
            if nums[i] != (i + 1):
                return i + 1
        
        # return n+1 if all in the list
        return n + 1