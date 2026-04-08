class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use stack to keep heights increasing (start_index, height)
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            start_index = i
            # pop if current height is lower
            while stack and heights[i] < stack[-1][1]:
                start_index, height = stack.pop()

                # update max_area: area = height * (i - index)
                curr_area = height * (i - start_index)
                max_area = max(max_area, curr_area)

            # push this node
            stack.append((start_index, heights[i]))
        
        while stack:
            start_index, height = stack.pop()
            curr_area = height * (n - start_index)
            max_area = max(max_area, curr_area)

        return max_area