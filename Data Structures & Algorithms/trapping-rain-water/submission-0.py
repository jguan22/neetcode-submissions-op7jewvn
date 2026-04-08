class Solution:
    def trap(self, height: List[int]) -> int:
        # use two pointers
        n = len(height)
        l = 0
        r = n - 1

        max_l = height[l]
        max_r = height[r]
        ans = 0

        # the amount of water depends on the minimum of max left/right bounds
        while l < r:
            # move and update left bound, then compute the water based on it 
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                ans += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                ans += max_r - height[r]
        
        return ans