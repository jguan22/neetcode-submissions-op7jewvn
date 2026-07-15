class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use a stack to track prev h
        # prev histogram stops at lower h: keep stack in increasing order
        stack = []      # (height, index)
        max_area = 0

        # linear scan: O(n)
        for i, h in enumerate(heights):
            prev_i = i

            while stack and stack[-1][0] >= h:
                prev_h, prev_i = stack.pop()
                
                # compute curr_area and update max
                curr_area = (i - prev_i) * prev_h
                max_area = max(max_area, curr_area)
            
            # extend curr histogram to the left
            stack.append((h, prev_i))
        
        # compute the histograms left in stack: O(n)
        n = len(heights)
        while stack:
            h, i = stack.pop()
            curr_area = (n - i) * h
            max_area = max(max_area, curr_area)

        return max_area