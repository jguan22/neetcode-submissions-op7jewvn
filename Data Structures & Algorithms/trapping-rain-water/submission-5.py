class Solution:
    def trap(self, height: List[int]) -> int:
        # water level depends on the lower side of both ends
        l, r = 0, len(height) - 1
        left_h, right_h = height[l], height[r]
        water = 0
        
        # two pointers: track both sides and move the one with lower height
        while l <= r:
            if left_h <= right_h:
                # update water level and water amount equals to water level - curr height
                left_h = max(left_h, height[l])
                water += (left_h - height[l])
                l += 1
                
            else:
                right_h = max(right_h, height[r])
                water += (right_h - height[r])
                r -= 1
        
        return water