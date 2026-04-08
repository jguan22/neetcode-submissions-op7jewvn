class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maintain the increasing stack (height, start)
        stack = []
        max_area = 0
        
        # the height of rectangle is limited by the lowest
        for i, height in enumerate(heights):
            start = i
            # if curr height is lower, previous height stops here (rectangle found)
            while stack and height < stack[-1][0]:
                pre, start = stack.pop()
                max_area = max(max_area, pre * (i - start))
            
            # mark the starting point of current rectangle
            stack.append((height, start))
        
        # compute the remaining rectangle in the stack
        n = len(heights)
        for height, i in stack:
            max_area = max(max_area, height * (n - i))

        return max_area