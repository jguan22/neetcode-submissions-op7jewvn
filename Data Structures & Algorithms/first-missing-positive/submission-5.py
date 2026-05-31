class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # bucket sort: move positive nums to its position (0-index)
        n = len(nums)
        i = 0
        
        while i < n:
            # swap num to its correct position
            correct_pos = nums[i] - 1
            if 0 <= correct_pos < n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
                continue

            i += 1

        # linear scan to find the first one not there
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        
        return n + 1