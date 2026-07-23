class Solution:
    def jump(self, nums: List[int]) -> int:
        # linear scan to check the range can be reached at each step: O(n)
        start, end = 0, 0
        n = len(nums)
        step = 0

        while end < n-1:
            # update step
            step += 1

            # update range
            new_end = end
            for i in range(start, end + 1):
                new_end = max(new_end, i + nums[i])
            
            start, end = end + 1, new_end

        return step
        