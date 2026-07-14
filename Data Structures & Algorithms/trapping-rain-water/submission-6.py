class Solution:
    def trap(self, height: List[int]) -> int:
        # water level depends on the lower bound of two
        l, r = 0, len(height) - 1
        left_bound, right_bound = height[l], height[r]
        water = 0
        
        # linear scan: O(n)
        while l <= r:
            # move the side with lower bound
            if left_bound < right_bound:
                # update water and bound
                left_bound = max(left_bound, height[l])
                water += (left_bound - height[l])
                l += 1
            else:
                right_bound = max(right_bound, height[r])
                water += (right_bound - height[r])
                r -= 1

        return water