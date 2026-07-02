class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy: find the highest index can be reached
        n = len(nums)
        start, end = 0, 0
        step = 0

        # loop until n-1 is reached: O(n)
        while end < n-1:
            step += 1

            # find the highest index to reach in curr range
            next_end = end
            for i in range(start, end+1):
                next_end = max(next_end, i + nums[i])
            
            start, end = end + 1, next_end
        
        return step