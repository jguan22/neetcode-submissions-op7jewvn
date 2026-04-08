class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # need to reach n-1
        # compute the furthest can go after curr_jump
        n = len(nums)
        max_reach = 0

        for i in range(n):
            # ith position is out of reach
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= n-1:
                return True
        
        return False