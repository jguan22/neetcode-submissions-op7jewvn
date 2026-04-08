class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # need to reach n-1
        # compute the furthest can go after curr_jump
        n = len(nums)
        start = 0
        curr_jump = nums[0]
        
        while curr_jump < n - 1:
            isForward = False
            # find the furthest option after this jump from i to max_jump
            for i in range(start, curr_jump+1):
                next_jump = i + nums[i]
                if next_jump > curr_jump:
                    curr_jump = next_jump
                    start = i
                    isForward = True
            
            if not isForward:
                return False
            
        
        return True