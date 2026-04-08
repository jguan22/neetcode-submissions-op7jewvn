class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a stack to keep decreasing order (temp, index)
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # when higher temperatrue shows up, pop pre and update the ans
            while stack and stack[-1][0] < temp:
                _, j = stack.pop()
                ans[j] = i - j
            
            stack.append((temp, i))
            
        return ans