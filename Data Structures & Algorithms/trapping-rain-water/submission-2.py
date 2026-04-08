class Solution:
    def trap(self, height: List[int]) -> int:
        # use monostack: pop previous height when a new height is higher
        stack = []
        total_area = 0
        
        for i, currH in enumerate(height):
            while stack and currH > height[stack[-1]]:
                low_index = stack.pop()

                if not stack:
                    break

                left_index = stack[-1]
                h = min(height[left_index], currH)
                total_area += ((i - left_index - 1) * (h - height[low_index]))
            
            stack.append(i)
        
        return total_area