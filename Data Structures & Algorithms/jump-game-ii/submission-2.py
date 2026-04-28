class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy: O(n)
        n = len(nums)
        start, curr_max = 0, 0
        step = 0
        while curr_max < n - 1:
            step += 1
            end = curr_max
            
            # check how far we can go by curr step (start to end)
            for i in range(start, end + 1):
                curr_max = max(curr_max, i + nums[i])
            
            start = end + 1
        
        return step