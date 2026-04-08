class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        max_jump = 0
        count = 0

        while max_jump < n-1:
            count += 1
            end = max_jump
            for i in range(start, end+1):
                curr_jump = i + nums[i]
                if curr_jump > max_jump:
                    max_jump = curr_jump
                    start = i + 1

        return count