class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # linear scan to update the range that can reach: O(n)
        start, end = 0, 0
        n = len(nums)
        while start <= end:
            # update right bound of range
            end = max(end, start + nums[start])

            # base case:
            if end >= n-1:
                return True
            
            start += 1
        
        return False
