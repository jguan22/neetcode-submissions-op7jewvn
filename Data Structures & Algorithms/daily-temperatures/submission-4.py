class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack and keep a decreasing order
        stack = []
        ans = [0] * len(temperatures)

        # loop through the list: O(n)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                index = stack.pop()
                ans[index] = i - index
            
            stack.append(i)
        
        return ans