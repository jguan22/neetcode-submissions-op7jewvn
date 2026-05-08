class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use mono stack to keep increasing order
        stack = []  # (height, index)
        max_area = 0

        for i, curr_h in enumerate(heights):
            index = i
            while stack and stack[-1][0] > curr_h:
                # pop anything higher and update area (histogram that stops here)
                # update index for curr h as curr histogram can extend further to left
                prev_h, index = stack.pop()

                # update max_area
                curr_area = (i - index) * prev_h
                max_area = max(max_area, curr_area)
            
            # insert curr height and index
            stack.append((curr_h, index))
        
        # compute area of each histogram left in stack
        n = len(heights)
        for h, i in stack:
            curr_area = (n - i) * h
            max_area = max(max_area, curr_area)

        return max_area