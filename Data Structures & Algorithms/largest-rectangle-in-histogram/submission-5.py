class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use a stack with ascending order: histogram stops with lower height
        stack = []  # (height, start_index)
        max_area = 0

        # first linear scan to scan the list
        for i, h in enumerate(heights):
            # 1. pop any higher height
            start = i
            while stack and stack[-1][0] >= h:
                # update area
                prev_h, start = stack.pop()
                curr_area = prev_h * (i - start)
                max_area = max(max_area, curr_area)
            
            # 2. insert curr height and extend to start index
            stack.append((h, start))
        
        # 3. second linear scan to calculate area of histograms that extend to the end
        n = len(heights)
        while stack:
            h, start = stack.pop()
            curr_area = h * (n - start)
            max_area = max(max_area, curr_area)

        return max_area