class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        i = 0
        n = len(nums)
        while i <= furthest:
            furthest = max(furthest, i+nums[i])
            if furthest >= n-1:
                return True
            i += 1
        
        return False