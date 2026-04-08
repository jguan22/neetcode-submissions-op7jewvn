class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use monostack to store (height, index)
        stack = []
        max_area = 0

        # use a sentinel 0 to pop and compute all histograms at the end
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and h <= stack[-1][0]:
                pre_h, pre_i = stack.pop()
                max_area = max(max_area, pre_h * (i - pre_i))
                start = pre_i
            
            stack.append((h, start))
        
        return max_area