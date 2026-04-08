class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers
        n = len(heights)
        l, r = 0, n-1
        maxArea = 0
        while l < r:
            currArea = (r-l) * min(heights[l], heights[r])
            maxArea = max(maxArea, currArea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea