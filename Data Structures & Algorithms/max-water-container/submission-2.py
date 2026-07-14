class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # water depends on the lower bound of two
        # two pointers: move the lower one each step and update max
        max_area = 0
        l, r = 0, len(heights) - 1

        # linear scan: O(n)
        while l < r:
            if heights[l] < heights[r]:
                h = heights[l]
                l += 1
            else:
                h = heights[r]
                r -= 1
                
            curr_area = h * (r - l + 1)
            max_area = max(max_area, curr_area)
        
        return max_area