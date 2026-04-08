class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use stack to track the height of each rectangle
        # since rectangle stops when the height gets lower, keep stack in increasing order
        stack = []  # (starting_index, height)
        max_area = 0
        for i, curr_height in enumerate(heights):
            index = i
            while stack and curr_height < stack[-1][1]:
                index, height = stack.pop()
                area = (i - index) * height
                max_area = max(max_area, area)

            stack.append((index, curr_height))
        
        n = len(heights)
        while stack:
            index, height = stack.pop()
            area = (n - index) * height
            max_area = max(max_area, area)
        
        return max_area