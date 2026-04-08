class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer
        n = len(height)
        area = 0
        
        # move the lower bound since water level depends on the lower one
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                area += (maxLeft - height[l])
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                area += (maxRight - height[r])
        
        return area