class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers: water level depends on the lowest one on both ends
        n = len(height)
        l, r = 0, n - 1
        left_bar, right_bar = height[l], height[r]
        water = 0

        while l <= r:
            if left_bar <= right_bar:
                left_bar = max(left_bar, height[l])
                water += (left_bar - height[l])
                l += 1
            else:
                right_bar = max(right_bar, height[r])
                water += (right_bar - height[r])
                r -= 1
        
        return water